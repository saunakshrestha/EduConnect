from django.urls import path
from admin_dashboard.views import AddStudentView

app_name = 'admin_dashboard'

urlpatterns = [
    path('entry/', AddStudentView.as_view(), name='entry_students'),

]