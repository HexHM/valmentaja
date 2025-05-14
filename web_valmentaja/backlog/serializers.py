from rest_framework import serializers
from .models import Task, TaskClass
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "completed", "priority", "task_class", "user"]
        extra_kwargs = {
            'title': {'help_text': 'Tehtävän nimi'},
            'description': {'help_text': 'Tehtävän kuvaus'},
            'completed': {'help_text': 'Onko tehtävä valmis'},
            'priority': {'help_text': 'Tehtävän prioriteetti'},
            'task_class': {'help_text': 'Tehtävän luokitus'},
            'user': {'help_text': 'Tehtävän käyttäjä'},
        }
    
    
class TaskClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskClass
        fields = ["id", "title"]
        
