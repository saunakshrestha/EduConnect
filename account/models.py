import logging
import random
import string

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


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', unique=True)
    username = models.CharField(verbose_name='Username', max_length=255)
    first_name = models.CharField(verbose_name='First Name', max_length=255, blank=True)
    middle_name = models.CharField(verbose_name='Middle Name', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone Number', unique=True)
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
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


