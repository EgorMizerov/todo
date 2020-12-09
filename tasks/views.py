import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task
from toDoList.settings import BASE_DIR
import json

# Create your views here.


def index(request):
    user = request.user
    filename = str(BASE_DIR) + '/static/js/tasks/events.json'
    dt = datetime.now()
    start_date = dt.strftime("%Y-%m-%d")

    # Если пользователь не аутентифицирован
    if user.username == "":
        return render(request, 'main/main.html')

    tasks_list = Task.objects.filter(user_name=user)
    if request.POST:
        task_text = request.POST.get("edesc")
        task_name = request.POST.get("ename")
        task_date = request.POST.get("edate")

        # Добавить задачу
        if request.POST.get("type") == "add-task":
            task_status = "выполянется"
            start_date = dt.strftime("%Y-%m-%d")
            # Ошибка какая-то ;(
            try:
                newTask = Task.objects.create(user_name=user, task_name=task_name, task_text=task_text, task_status=task_status,
                                              end_date=task_date, start_date=start_date)
                newTask.save()
            except:
                pass

            with open(filename, encoding='utf-8') as f:
                taskslistJSON = json.load(f)
                print(taskslistJSON)
                jsonstartdate = dt.strftime("%Y-%m-%d")
                newtaskjson = {"user_name": user.username,
                               "title": task_name,
                               "description": task_text,
                               "start": jsonstartdate,
                               "end": task_date
                               }
                taskslistJSON.append(newtaskjson)
                os.remove(filename)
            with open(filename, 'w') as f:
                json.dump(taskslistJSON, f)

            return render(request, 'tasks/index.html', {'tasks_list': tasks_list, "date": start_date})

        # Изменить задачу
        if request.POST.get("type") == "edit-task":
            task_id = request.POST.get("eid")

            try:
                task = Task.objects.filter(id=int(task_id)).update(task_name=task_name, task_text=task_text, end_date=task_date)
            except:
                raise Http404("Задача не найдена")

            return render(request, 'tasks/index.html', {'tasks_list': tasks_list, "date": start_date})

        # Закончить задачу
        if request.POST.get("type") == "delete-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.filter(id=int(task_id)).update(task_status="Выполнено")
                print(task)
            except:
                raise Http404("Задача не найдена")
            return render(request, 'tasks/index.html', {'tasks_list': tasks_list, "date": start_date})

        # Начать задачу занаво
        if request.POST.get("type") == "restart-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.filter(id=int(task_id)).update(task_status="Не выполнено")
            except:
                raise Http404("Задача не найдена")
            return render(request, 'tasks/index.html', {'tasks_list': tasks_list, "date": start_date})

        # Найти задачу
        if request.POST.get("type") == "search-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.get(id=int(task_id))
            except:
                raise Http404("Задача не найдена")
            return render(request, 'tasks/task.html', {'task': task, "date": start_date})

        # Показать задачи
        if request.POST.get("type") == "display-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.filter(start_date=str(start_date))
            except:
                raise Http404("Задачи не найдена")
            return render(request, 'tasks/displayTask.html', {'tasks_list': task, "date": start_date})

    return render(request, 'tasks/index.html', {'tasks_list': tasks_list, "date": start_date})


def login(request):
    return render(request, 'tasks/index.html')
