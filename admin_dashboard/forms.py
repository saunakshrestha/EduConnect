from django import forms
from admin_dashboard.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'user',
            'profile_pic',
            'permanent_address',
            'temporary_address',
            'intake_month',
            'intake_year',
            'dob',
            'gender',
            'emergency_contact',
            'education_level',
            'notifications_enabled',
            'status',
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.Select(attrs={'class': 'form-select'}),
            'temporary_address': forms.Select(attrs={'class': 'form-select'}),
            'intake_month': forms.Select(attrs={'class': 'form-select'}),
            'intake_year': forms.Select(attrs={'class': 'form-select'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            'notifications_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }