from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    
    priority=models.IntegerField(default=0)
    
    additional_info = models.CharField(max_length=200, default="", blank=True)
    
    task_class = models.ForeignKey('TaskClass', on_delete=models.SET_DEFAULT, default=None, null=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
class TaskClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    
    def __str__(self):
        return "Kommentti Käyttäjältä " + self.user.username + " tehtäävän " + self.task.title


class Maps(models.Model):
    title=models.CharField(max_length=200)
    priority=models.IntegerField(default=0)
    task = models.ForeignKey(Task, related_name="maps", on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.title