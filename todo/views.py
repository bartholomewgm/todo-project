from django.http import HttpResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    result = "\n".join([f"{t.id}. {t.title} - {t.completed}" for t in tasks])
    return HttpResponse(result or "No tasks yet")