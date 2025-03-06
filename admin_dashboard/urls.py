from django.urls import path
from admin_dashboard.views import AddStudentView
from admin_dashboard.views import get_districts

app_name = 'admin_dashboard'

urlpatterns = [
    path('entry/', AddStudentView.as_view(), name='entry_students'),
    path('get_districts/', get_districts, name='get_districts'),

]