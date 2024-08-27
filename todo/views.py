from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.
def addTask(requests):
    task = requests.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

# def updateTask(requests):
#     update = requests.POST['task']
#     Task.objects.delete(task=update)
#     return redirect('home')