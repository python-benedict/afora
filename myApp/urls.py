from django.urls import path
from . import views

urlpatterns = [
    path('', views.AttendanceListView(), name='index'), 
]