from django import forms
from .models import Task
 
class TaskEditForm(forms.Form):
    name = forms.CharField(label="Tehtävän nimi", max_length=200)
    description = forms.CharField(label="Kuvaus", widget=forms.Textarea)
    priority = forms.IntegerField(label="Prioriteetti")
    
class TaskEditModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
class MyModel2(forms.Form):
   team = forms.CharField(widget=forms.Select)