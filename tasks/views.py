from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task

# Create your views here.


def index(request):
    user = request.user
    tasks_list = Task.objects.filter(user_name=user)
    if request.POST:
        task_text = request.POST.get("edesc")
        task_name = request.POST.get("ename")
        task_date = request.POST.get("edate")


        if request.POST.get("type") == "add-task":
            task_status = "выполянется"
            dt = datetime.now()
            start_date = dt.strftime("%d/%m/%Y %H:%M %p")

            # Ошибка какая-то ;(
            try:
                newTask = Task.objects.create(user_name=user, task_name=task_name, task_text=task_text, task_status=task_status,
                                              end_date=task_date, start_date=start_date)
                newTask.save()
            except:
                pass

            return render(request, 'tasks/index.html', {'tasks_list': tasks_list})

        if request.POST.get("type") == "edit-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.filter(id=int(task_id)).update(task_name=task_name, task_text=task_text, end_date=task_date)
            except:
                raise Http404("Задача не найдена")
            # try:
                print(task.task_name)
            # except:
            #     pass
            return render(request, 'tasks/index.html', {'tasks_list': tasks_list})

        if request.POST.get("type") == "delete-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.filter(id=int(task_id)).update(task_status="Выполнено")
                print(task)
            except:
                raise Http404("Задача не найдена")
            return render(request, 'tasks/index.html', {'tasks_list': tasks_list})

        if request.POST.get("type") == "restart-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.filter(id=int(task_id)).update(task_status="Не выполнено")
            except:
                raise Http404("Задача не найдена")
            return render(request, 'tasks/index.html', {'tasks_list': tasks_list})

        if request.POST.get("type") == "search-task":
            task_id = request.POST.get("eid")
            try:
                task = Task.objects.get(id=int(task_id))
            except:
                raise Http404("Задача не найдена")
            return render(request, 'tasks/task.html', {'task': task})

    return render(request, 'tasks/index.html', {'tasks_list': tasks_list})


def login(request):
    return render(request, 'tasks/index.html')