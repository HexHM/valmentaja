from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
#from .models import Task, TaskClass, Comment, Maps
from django.contrib.auth.decorators import login_required
#from .forms import TaskEditForm, TaskEditModelForm
from rest_framework import generics
#from .serializers import TaskSerializer, TaskClassSerializer
from rest_framework.permissions import IsAuthenticated
 
# Create your views here.
def home (request):
 #   if request.user.is_superuser or request.user.is_staff:
#        return redirect('task_list')
#    else:
#        return redirect('task_maps')
    return

def task_list(request):
    return HttpResponse("Tässä ovat kaikki tehtävät!")