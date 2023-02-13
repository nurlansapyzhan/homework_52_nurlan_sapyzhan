from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_list.models import Task


def add_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'finish_date': request.POST.get('finish_date')
    }
    Task.objects.create(**task_data)
    return redirect('/')
