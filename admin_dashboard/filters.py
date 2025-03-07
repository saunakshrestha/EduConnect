import django_filters
from django import forms
from admin_dashboard.models import Student, Address

class StudentFilter(django_filters.FilterSet):
    # Identification
    unique_id = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    middle_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    profile_pic = django_filters.CharFilter(lookup_expr='icontains')
    # Permanent Address
    permanent_address__province = django_filters.CharFilter(lookup_expr='icontains')
    permanent_address__district = django_filters.CharFilter(lookup_expr='icontains')
    permanent_address__local_unit_type = django_filters.CharFilter(lookup_expr='icontains')
    permanent_address__local_unit_name = django_filters.CharFilter(lookup_expr='icontains')
    permanent_address__ward_no = django_filters.CharFilter(lookup_expr='icontains')
    permanent_address__tole = django_filters.CharFilter(lookup_expr='icontains')
    permanent_address__postal_code = django_filters.CharFilter(lookup_expr='icontains')
    # Temporary Address
    temporary_address__province = django_filters.CharFilter(lookup_expr='icontains')
    temporary_address__district = django_filters.CharFilter(lookup_expr='icontains')
    temporary_address__local_unit_type = django_filters.CharFilter(lookup_expr='icontains')
    temporary_address__local_unit_name = django_filters.CharFilter(lookup_expr='icontains')
    temporary_address__ward_no = django_filters.CharFilter(lookup_expr='icontains')
    temporary_address__tole = django_filters.CharFilter(lookup_expr='icontains')
    temporary_address__postal_code = django_filters.CharFilter(lookup_expr='icontains')
    # Personal Information
    intake_month = django_filters.CharFilter(lookup_expr='icontains')
    intake_year = django_filters.CharFilter(lookup_expr='icontains')
    dob = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = django_filters.CharFilter(lookup_expr='icontains')
    emergency_contact = django_filters.CharFilter(lookup_expr='icontains')
    education_level = django_filters.CharFilter(lookup_expr='icontains')
    notifications_enabled = django_filters.BooleanFilter()
    status = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))
    updated_at = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student
        fields = [
            'unique_id',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'phone',
            'profile_pic',
            'permanent_address__province',
            'permanent_address__district',
            'permanent_address__local_unit_type',
            'permanent_address__local_unit_name',
            'permanent_address__ward_no',
            'permanent_address__tole',
            'permanent_address__postal_code',
            'temporary_address__province',
            'temporary_address__district',
            'temporary_address__local_unit_type',
            'temporary_address__local_unit_name',
            'temporary_address__ward_no',
            'temporary_address__tole',
            'temporary_address__postal_code',
            'intake_month',
            'intake_year',
            'dob',
            'gender',
            'emergency_contact',
            'education_level',
            'notifications_enabled',
            'status',
            'created_at',
            'updated_at'
        ]
