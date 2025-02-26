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
    intake_month = django_filters.CharFilter(
        widget=forms.Select(
            choices=[('january', 'January'), ('febuary', 'Febuary'), ('march', 'March'), ('april', 'April'),
                     ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'),
                     ('december', 'December')],
            attrs={
                'class': 'form-select'
            })
    )
    intake_year = django_filters.CharFilter(
        widget=forms.Select(
            choices=
            [('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'),
             ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'),
             ('2028', '2028'), ('2029', '2029'), ('2030', '2030')],
            attrs={
                'class': 'form-select'
            })
    )

    education_level = django_filters.CharFilter(
        widget=forms.Select(
            choices=[('+2', '+2'), ('bachelor', 'Bachelor'), ('master', 'Master'), ('phd', 'PhD')],
            attrs={
                'class': 'form-select'
            })
    )

    class Meta:
        model = Student
        fields = [
            'unique_id',
            'user__username',
            'user__email',
            'profile__phone',
            'admission_date',
            'graduation_date',
            'status',
            'created_at',
            'updated_at',
            'intake_month',
            'intake_year',
            'education_level',
        ]
