from django.db import models
from account.models import Users, Profile
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


class Student(models.Model):
    STATUS_CHOICES = [
        ('', 'Select Status'),
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('graduated', 'Graduated'),
        ('dropped', 'Dropped Out'),
        ('suspended', 'Suspended')
    ]

    # Identification
    unique_id = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)

    # Relations
    user = models.OneToOneField(Users, on_delete=models.SET_NULL,
                                related_name="student_detail", null=True, blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL,
                                   related_name="student_profile", null=True, blank=True)

    # Status
    is_admitted = models.BooleanField(default=False)
    admission_date = models.DateField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Student: {self.student_id} - {self.user.name if self.user else 'No Name'}"

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
        ('parent_citizenship', 'Parent Citizenship'),
        ('plus_two_character', '+2 Character'),
        ('plus_two_transcript', '+2 Transcript'),
        ('tenth_character', '10th Character'),
        ('ward_recommendation', 'Ward Recommendation'),
        ('jlct', 'JLCT Certificate'),
    ]

    VERIFICATION_STATUS = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected')
    ]

    # Relations and Type
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)

    # Document Details
    file = models.FileField(upload_to=document_file_path)
    expiry_date = models.DateField(null=True, blank=True)
    score = models.CharField(max_length=20, null=True, blank=True)  # For JLCT or other scored documents
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
