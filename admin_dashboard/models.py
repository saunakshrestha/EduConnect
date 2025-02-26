from django.db import models
from account.models import Users
from datetime import datetime
from django.utils import timezone

import uuid
import hashlib


def document_file_path(instance, filename):
    """
    documents/document_type/student_id/YYYY/MM/DD/filename
    """
    now = datetime.now()
    return (f'documents/{instance.document_type}/'
            f'{instance.student.unique_id}/{now.year}/{now.month}/{now.day}/{filename}')


def generate_custom_uuid(instance):
    # Combine user data to create a unique string
    unique_string = f"{instance.user.username}{instance.user.email}{instance.user.created}{timezone.now()}"
    # Create a UUID based on the hash of the unique string
    return unique_string


class Address(models.Model):
    # Choices for Province
    PROVINCE_CHOICES = [
        ('Province 1', 'Province 1'),
        ('Madhesh Pradesh', 'Madhesh Pradesh'),
        ('Bagmati Pradesh', 'Bagmati Pradesh'),
        ('Gandaki Pradesh', 'Gandaki Pradesh'),
        ('Lumbini Pradesh', 'Lumbini Pradesh'),
        ('Karnali Pradesh', 'Karnali Pradesh'),
        ('Sudurpashchim Pradesh', 'Sudurpashchim Pradesh'),
    ]

    # Choices for Local Unit Type
    LOCAL_UNIT_TYPE_CHOICES = [
        ('Metropolitan', 'Metropolitan City'),
        ('Sub-Metropolitan', 'Sub-Metropolitan City'),
        ('Municipality', 'Municipality'),
        ('Rural Municipality', 'Rural Municipality'),
    ]

    # Choices for Districts (Example - Full List Needs to be Added)
    DISTRICT_CHOICES = [
        # Province 1
        ('Bhojpur', 'Bhojpur'),
        ('Dhankuta', 'Dhankuta'),
        ('Ilam', 'Ilam'),
        ('Jhapa', 'Jhapa'),
        ('Khotang', 'Khotang'),
        ('Morang', 'Morang'),
        ('Okhaldhunga', 'Okhaldhunga'),
        ('Panchthar', 'Panchthar'),
        ('Sankhuwasabha', 'Sankhuwasabha'),
        ('Solukhumbu', 'Solukhumbu'),
        ('Sunsari', 'Sunsari'),
        ('Taplejung', 'Taplejung'),
        ('Terhathum', 'Terhathum'),
        ('Udayapur', 'Udayapur'),

        # Madhesh Pradesh
        ('Bara', 'Bara'),
        ('Dhanusha', 'Dhanusha'),
        ('Mahottari', 'Mahottari'),
        ('Parsa', 'Parsa'),
        ('Rautahat', 'Rautahat'),
        ('Saptari', 'Saptari'),
        ('Sarlahi', 'Sarlahi'),
        ('Siraha', 'Siraha'),

        # Bagmati Pradesh
        ('Bhaktapur', 'Bhaktapur'),
        ('Chitwan', 'Chitwan'),
        ('Dhading', 'Dhading'),
        ('Dolakha', 'Dolakha'),
        ('Kathmandu', 'Kathmandu'),
        ('Kavrepalanchok', 'Kavrepalanchok'),
        ('Lalitpur', 'Lalitpur'),
        ('Makwanpur', 'Makwanpur'),
        ('Nuwakot', 'Nuwakot'),
        ('Ramechhap', 'Ramechhap'),
        ('Rasuwa', 'Rasuwa'),
        ('Sindhuli', 'Sindhuli'),
        ('Sindhupalchok', 'Sindhupalchok'),

        # Gandaki Pradesh
        ('Baglung', 'Baglung'),
        ('Gorkha', 'Gorkha'),
        ('Kaski', 'Kaski'),
        ('Lamjung', 'Lamjung'),
        ('Manang', 'Manang'),
        ('Mustang', 'Mustang'),
        ('Myagdi', 'Myagdi'),
        ('Nawalpur', 'Nawalpur'),
        ('Parbat', 'Parbat'),
        ('Syangja', 'Syangja'),
        ('Tanahun', 'Tanahun'),

        # Lumbini Pradesh
        ('Arghakhanchi', 'Arghakhanchi'),
        ('Banke', 'Banke'),
        ('Bardiya', 'Bardiya'),
        ('Dang', 'Dang'),
        ('Eastern Rukum', 'Eastern Rukum'),
        ('Gulmi', 'Gulmi'),
        ('Kapilvastu', 'Kapilvastu'),
        ('Parasi', 'Parasi'),
        ('Palpa', 'Palpa'),
        ('Pyuthan', 'Pyuthan'),
        ('Rolpa', 'Rolpa'),
        ('Rupandehi', 'Rupandehi'),

        # Karnali Pradesh
        ('Dailekh', 'Dailekh'),
        ('Dolpa', 'Dolpa'),
        ('Humla', 'Humla'),
        ('Jajarkot', 'Jajarkot'),
        ('Jumla', 'Jumla'),
        ('Kalikot', 'Kalikot'),
        ('Mugu', 'Mugu'),
        ('Salyan', 'Salyan'),
        ('Surkhet', 'Surkhet'),
        ('Western Rukum', 'Western Rukum'),

        # Sudurpashchim Pradesh
        ('Achham', 'Achham'),
        ('Baitadi', 'Baitadi'),
        ('Bajhang', 'Bajhang'),
        ('Bajura', 'Bajura'),
        ('Dadeldhura', 'Dadeldhura'),
        ('Darchula', 'Darchula'),
        ('Doti', 'Doti'),
        ('Kailali', 'Kailali'),
        ('Kanchanpur', 'Kanchanpur'),
    ]

    province = models.CharField(max_length=50, choices=PROVINCE_CHOICES)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    local_unit_type = models.CharField(max_length=20, choices=LOCAL_UNIT_TYPE_CHOICES)
    local_unit_name = models.CharField(max_length=50)  # Name of Metropolitan, Municipality, etc.
    ward_no = models.PositiveIntegerField()
    tole = models.CharField(max_length=100, blank=True, null=True)  # Optional
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.local_unit_name}, {self.district}, {self.province} ({self.address_type})"


def profile_location(instance, filename):
    return f"profile/pictures/{instance.user.username}/{filename}"


class Student(models.Model):
    STATUS_CHOICES = [
        ('', 'Select Status'),
        ('hold', 'Hold'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('rejected', 'Rejected'),
        ('graduated', 'Graduated'),
        ('transferred', 'Transferred'),
        ('withdrawn', 'Withdrawn'),
        ('pending', 'Pending'),
    ]

    # Identification
    unique_id = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)

    # Relations
    user = models.OneToOneField(Users, on_delete=models.SET_NULL,
                                related_name="student_detail", null=True, blank=True)
    profile_pic = models.FileField(upload_to=profile_location, verbose_name="Profile Picture")
    permanent_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name="permanent_address",
                                          null=True, blank=True)
    temporary_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name="temporary_address",
                                          null=True, blank=True)
    intake_month = models.CharField(max_length=20, choices=[('january', 'January'), ('febuary', 'Febuary'),
                                                            ('march', 'March'), ('april', 'April'), ('may', 'May'),
                                                            ('june', 'June'), ('july', 'July'), ('august', 'August'),
                                                            ('september', 'September'), ('october', 'October'),
                                                            ('november', 'November'), ('december', 'December')],
                                    blank=True, null=True)
    intake_year = models.CharField(max_length=20, choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'),
                                                           ('2023', '2023'), ('2024', '2024'), ('2025', '2025'),
                                                           ('2026', '2026'), ('2027', '2027'), ('2028', '2028'),
                                                           ('2029', '2029'), ('2030', '2030')], blank=True, null=True)

    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True, choices=[('+2', '+2'),
                                                                                       ('bachelor', 'Bachelor'),
                                                                                       ('master', 'Master'),
                                                                                       ('phd', 'PhD')])
    notifications_enabled = models.BooleanField(default=False)
    updated = models.DateTimeField(default=timezone.now)

    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Student: {self.unique_id} - {self.user.name if self.user else 'No Name'}"

    def get_document(self, document_type):
        """Get latest version of a specific document"""
        return self.documents.filter(
            document_type=document_type,
            is_latest=True
        ).first()

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = generate_custom_uuid(self)
        super().save(*args, **kwargs)


class Document(models.Model):
    DOCUMENT_TYPES = [
        ('passport', 'Passport'),
        ('student_citizenship', 'Student Citizenship'),
        ('parent_citizenship', 'Parent Citizenship'),  ##
        ('plus_two_character', '+2 Character'),
        ('plus_two_transcript', '+2 Transcript'),
        ('tenth_character', '10th Character'),
        ('ward_recommendation', 'Ward Recommendation'),  ##
        ('jlct', 'JLCT Certificate'),  ##
    ]

    VERIFICATION_STATUS = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected')
    ]

    # Relations and Type
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS, default='pending')
    verified_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True)

    # Version tracking
    version = models.PositiveIntegerField(default=1)
    is_latest = models.BooleanField(default=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'document_type', 'version']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.document_type} - {self.student.unique_id}"


class DocumentFile(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=document_file_path)
    expiry_date = models.DateField(null=True, blank=True)
    score = models.CharField(max_length=20, null=True, blank=True)  # For JLCT or other scored documents

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"File for {self.document.document_type} - {self.document.student.unique_id}"
