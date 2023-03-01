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
    

@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        start_date = date.today() - timedelta(days=7)
        end_date = date.today()
        attendances = Attendance.objects.filter(student=student, date__range=[start_date, end_date]).order_by('-date')
        context['attendances'] = attendances
        return context

@method_decorator(staff_member_required, name='dispatch')
class AttendanceCreateView(CreateView):
    model = Attendance
    fields = ['student', 'date', 'present']
    success_url = reverse_lazy('attendance_list')
    template_name = 'attendance_form.html'
    

@method_decorator(staff_member_required, name='dispatch')
class AttendanceUpdateView(UpdateView):
    model = Attendance
    fields = ['student', 'date', 'present']
    success_url = reverse_lazy('attendance_list')
    template_name = 'attendance_form.html'
    

@method_decorator(staff_member_required, name='dispatch')
class AttendanceDeleteView(DeleteView):
    model = Attendance
    success_url = reverse_lazy('attendance_list')
    template_name = 'attendance_confirm_delete.html'