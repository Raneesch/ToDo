
from django.shortcuts import render # type: ignore
from todo.models import Task


def home(request):  
    
    task=Task.objects.filter(is_completed=False)
    completed_task = Task.objects.filter(is_completed = True)
    
    context = {
        'task' : task,
        'completed_task' : completed_task
    }
    
    return render(request,'home-todo.html',context)
