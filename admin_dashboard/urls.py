from django.urls import path
from student.views import AddStudentView

app_name = 'student'

urlpatterns = [
    path('entry/', AddStudentView.as_view(), name='entry_students'),

]