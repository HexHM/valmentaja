from django.urls import path
from .views import home, task_list, task_maps
from . import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Task Planner rajapintadokumentaatio",
      default_version='v1',
      description="Tehtäväkorttisovelluksen API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@taskplanner.local"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('joukkoeet', home, name='home'),
    path('tasks/', task_list, name='task_list'),
    path('maps', task_maps, name='task_maps'),
    path("register_user/", views.register, name="register_user"),
    ]