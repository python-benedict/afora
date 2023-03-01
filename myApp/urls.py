from django.urls import path
from . import views

urlpatterns = [
    path('', views.AttendanceListView.as_view(), name='index'), 
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'), 
    path('attendance_create/', views.AttendanceCreateView.as_view(), name='attendance_create'), 
    path('<int:pk>/', views.AttendanceUpdateView.as_view(), name='attendance_update'), 
    path('<int:pk>/', views.AttendanceDeleteView.as_view(), name='attendance_update'), 
]