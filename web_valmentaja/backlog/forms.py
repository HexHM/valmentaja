from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
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
   
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    