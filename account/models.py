import hashlib
import logging
import random
import string
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db.models.query import QuerySet
from django.utils import timezone
from django.db import models

logger = logging.getLogger('educonnect_logger')


# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        if password is None:
            s_chars = 10  # number of characters in the string.
            # call random.choices() string module to find the string in Uppercase + numeric data.
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=s_chars))
        user.set_password(password)
        user.save()
        return user

    # def create_supervisor(self, email, username, password=None, **other_fields):
    # other_fields.setdefault('is_staff', False)
    # other_fields.setdefault('is_superuser', False)
    # other_fields.setdefault('is_active', False)
    #
    # user = self.create_user(email=email, username=username, password=password, **other_fields)
    # groups = Group.objects.all()
    # user.groups.add(*groups)
    # return user

    def create_superuser(self, email, username, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is False:
            raise ValueError('Superuser must be assigned is_staff = True')

        if other_fields.get('is_superuser') is False:
            raise ValueError('Superuser must be assigned is_superuser = True')
        if not password:
            password = f'{username}@ekg'
        user = self.create_user(email=email, username=username, password=password, **other_fields)
        try:
            groups = Group.objects.all()
            user.groups.add(*groups)
        except Exception as e:
            logger.exception(stack_info=False, msg=e.args)
        return user

    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


def location(instance, filename):
    return f'profile/{instance.username}/{filename}'


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', unique=True)
    username = models.CharField(verbose_name='Username', max_length=255)
    name = models.CharField(verbose_name='Name', max_length=255, blank=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True, auto_now=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    invalid_logins = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_set', blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = CustomAccountManager()

    def get_fullname(self):
        return f'{self.name}'

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


def profile_location(instance, filename):
    return f"profile/pictures/{instance.user.username}/{filename}"


def generate_custom_uuid(instance):
    # Combine user data to create a unique string
    unique_string = f"{instance.user.username}{instance.user.email}{instance.user.created}{timezone.now()}"
    # Create a UUID based on the hash of the unique string
    return uuid.UUID(hashlib.md5(unique_string.encode()).hexdigest())


class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.SET_NULL, related_name="user_profile", null=True, blank=True)
    unique_id = models.UUIDField(default=generate_custom_uuid, editable=False, unique=True)

    profile_pic = models.FileField(upload_to=profile_location, verbose_name="Profile Picture")
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              blank=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    social_media_links = models.JSONField(blank=True, null=True)  # e.g., {"twitter": "username"}
    education_level = models.CharField(max_length=100, blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    notifications_enabled = models.BooleanField(default=True)
    updated = models.DateTimeField(default=timezone.now)

    def profile_pic_url(self):
        if self.profile_pic:
            return self.profile_pic.name
        return f"{settings.STATIC_URL}/assets_new/images/user.png"

    def __str__(self):
        return f"Profile of {self.user.name}"


class Student(models.Model):
    user = models.OneToOneField(Users, on_delete=models.SET_NULL, related_name="student_detail", null=True, blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, related_name="student_detail",
                                   null=True, blank=True)
    is_admitted = models.BooleanField(default=False)
    admission_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Student: {self.user.name} {self.user.name}"
