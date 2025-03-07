# Generated by Django 4.2 on 2025-03-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0003_alter_student_profile_pic_alter_student_unique_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='test@saunak.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Middle Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='unique_id',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
