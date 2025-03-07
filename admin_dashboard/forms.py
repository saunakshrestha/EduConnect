from django import forms

from account.models import Users
from admin_dashboard.models import Student, Address

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):

    def save(self, commit=True):

        # Create Student (linking User and Address)
        student = super().save(commit=False)  # Don't save to DB yet

        if commit:
            student.save()

        return student

    class Meta:
        model = Student
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'phone',
            'email',
            'profile_pic',
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
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'intake_month': forms.Select(attrs={'class': 'form-select'}),
            'intake_year': forms.Select(attrs={'class': 'form-select'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            'notifications_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'province',
            'district',
            'local_unit_type',
            'local_unit_name',
            'ward_no',
            'tole',
            'postal_code',
        ]
        widgets = {
            'province': forms.Select(attrs={'class': 'form-select'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'local_unit_type': forms.Select(attrs={'class': 'form-select'}),
            'local_unit_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ward_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'tole': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }