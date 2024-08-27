from django.db import models

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.task

    
