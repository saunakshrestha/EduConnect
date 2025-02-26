from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from student.forms import StudentForm

from student.filters import StudentFilter
from student.models import Student
import logging

logger = logging.getLogger('educonnect_logger')


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        logger.info(request.GET)
        try:
            student_filter = StudentFilter(request.GET, queryset=Student.objects.all())
            logger.info(f"User {request.user.username} accessed the student home page.")
            return render(request, 'student/home.html', {'filter': student_filter})
        except Exception as e:
            logger.error(f"Error: {e}")
            return redirect('home')
class AddStudentView(View):
    def get(self, request, *args, **kwargs):
        form = StudentForm()
        return render(request, 'student/entry_students/entry_student.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'student/entry_students/entry_student.html', {'form': form})