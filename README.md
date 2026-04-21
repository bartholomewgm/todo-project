# Django Todo Project

Простое todo-приложение на Django с использованием ORM.

---

## 1. Создание проекта

mkdir todo_project
cd todo_project

python -m venv venv
venv\Scripts\activate   # Windows

# venv/Scripts/activate

pip install django

django-admin startproject todo_project .
python manage.py runserver

---

## 2. Создание приложения

python manage.py startapp todo

Добавить в settings.py:

INSTALLED_APPS = [
    ...
    'todo',
]

---

## 3. Маршруты

todo_project/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]

todo/urls.py:

from django.urls import path

urlpatterns = []

---

## 4. Модель

todo/models.py:

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

---

## 5. Миграции

python manage.py makemigrations
python manage.py migrate

---

## 6. Django shell (ORM)

python manage.py shell

from todo.models import Task

Task.objects.create(title="Task 1", description="First")
Task.objects.create(title="Task 2", description="Second")
Task.objects.create(title="Task 3", description="Third")

Task.objects.all()

task = Task.objects.get(id=1)
task.completed = True
task.save()

task = Task.objects.get(id=2)
task.delete()

---

## 7. Запуск

python manage.py runserver
