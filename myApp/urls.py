from django.urls import path
from . import views

urlpatterns = [
    path('', views.AttendanceListView.as_view(), name='index'), 
]