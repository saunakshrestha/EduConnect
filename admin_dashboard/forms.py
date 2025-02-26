from django import forms

from account.models import Users
from admin_dashboard.models import Student, Address

class StudentForm(forms.ModelForm):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()

    permanent_address_province = forms.ChoiceField(choices=Address.PROVINCE_CHOICES)
    permanent_address_district = forms.ChoiceField(choices=Address.DISTRICT_CHOICES)
    permanent_address_local_unit = forms.CharField()
    permanent_address_ward_no = forms.IntegerField()

    def save(self, commit=True):
        # Create User
        user = Users.objects.create(
            email=self.cleaned_data['email'],
            username=self.cleaned_data['email'].split('@')[0],  # Generating username from email
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone=self.cleaned_data['phone'],
        )

        # Create Address
        permanent_address = Address.objects.create(
            province=self.cleaned_data['permanent_address_province'],
            district=self.cleaned_data['permanent_address_district'],
            local_unit_name=self.cleaned_data['permanent_address_local_unit'],
            ward_no=self.cleaned_data['permanent_address_ward_no']
        )

        # Create Student (linking User and Address)
        student = super().save(commit=False)  # Don't save to DB yet
        student.user = user
        student.permanent_address = permanent_address

        if commit:
            student.save()

        return student

    class Meta:
        model = Student
        fields = [
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
