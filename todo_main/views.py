
from django.shortcuts import render # type: ignore
from todo.models import Task


def home(request):  
    
    task=Task.objects.filter(is_completed=False)
    
    context = {
        'task' : task
    }
    
    return render(request,'home-todo.html',context)