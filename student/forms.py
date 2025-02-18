from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'is_admitted',
            'admission_date',
            'graduation_date',
            'status'
        ]
        widgets = {
            'is_admitted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'admission_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'graduation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }