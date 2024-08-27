from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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

def mark_as_done(requests,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')