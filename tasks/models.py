from django.db import models

# Create your models here.


# Task Model
class Task(models.Model):
    user_name = models.CharField('Имя владельца задачаи', max_length=20)
    task_name = models.CharField('Название задачи', max_length=60)
    task_text = models.TextField('Описание задачи')
    task_status = models.CharField('Статус задачи', max_length=20)
    end_date = models.TextField('Дата окончания')
    start_date = models.TextField('Дата создания')

    def __str__(self):
        return self.task_name