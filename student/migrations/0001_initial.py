# Generated by Django 4.2 on 2025-02-18 01:35

from django.db import migrations, models
import django.db.models.deletion
import student.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.UUID('e93aedf4-1385-4c1a-b12a-c41ba4e9c47d'), editable=False, unique=True)),
                ('is_admitted', models.BooleanField(default=False)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('graduated', 'Graduated'), ('dropped', 'Dropped Out'), ('suspended', 'Suspended')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_profile', to='account.profile')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_detail', to='account.users')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('passport', 'Passport'), ('student_citizenship', 'Student Citizenship'), ('parent_citizenship', 'Parent Citizenship'), ('plus_two_character', '+2 Character'), ('plus_two_transcript', '+2 Transcript'), ('tenth_character', '10th Character'), ('ward_recommendation', 'Ward Recommendation'), ('jlct', 'JLCT Certificate')], max_length=50)),
                ('file', models.FileField(upload_to="student/documents/%Y/%m/%d")),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=20, null=True)),
                ('verification_status', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('is_latest', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='student.student')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.users')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('student', 'document_type', 'version')},
            },
        ),
    ]
