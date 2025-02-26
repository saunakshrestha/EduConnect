import uuid
import django_filters
from django import forms
from admin_dashboard.models import Student

class StudentFilter(django_filters.FilterSet):
    unique_id = django_filters.UUIDFilter(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Student ID'
        })
    )
    user__username = django_filters.CharFilter(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
    )
    user__email = django_filters.CharFilter(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    )
    profile__phone = django_filters.CharFilter(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Phone'
        })
    )
    is_admitted = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )
    admission_date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    graduation_date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    status = django_filters.CharFilter(
        widget=forms.Select(
            choices=Student.STATUS_CHOICES,
            attrs={
                'class': 'form-select'
            })
    )
    created_at = django_filters.DateFromToRangeFilter(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    updated_at = django_filters.DateFromToRangeFilter(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )

    class Meta:
        model = Student
        fields = [
            'unique_id',
            'user__username',
            'user__email',
            'profile__phone',
            'is_admitted',
            'admission_date',
            'graduation_date',
            'status',
            'created_at',
            'updated_at',
        ]