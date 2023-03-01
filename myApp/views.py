from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date, timedelta
from .models import Student, Attendance
# Create your views here.


class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list.html'

    def get_queryset(self):
        start_date = date.today() - timedelta(days=7)
        end_date = date.today()
        return Attendance.objects.filter(date__range=[start_date, end_date]).order_by('-date')