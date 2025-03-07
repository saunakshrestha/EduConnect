# Generated by Django 4.2 on 2025-02-26 17:05

import admin_dashboard.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_remove_users_name_users_first_name_users_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('Province 1', 'Province 1'), ('Madhesh Pradesh', 'Madhesh Pradesh'), ('Bagmati Pradesh', 'Bagmati Pradesh'), ('Gandaki Pradesh', 'Gandaki Pradesh'), ('Lumbini Pradesh', 'Lumbini Pradesh'), ('Karnali Pradesh', 'Karnali Pradesh'), ('Sudurpashchim Pradesh', 'Sudurpashchim Pradesh')], max_length=50)),
                ('district', models.CharField(choices=[('Bhojpur', 'Bhojpur'), ('Dhankuta', 'Dhankuta'), ('Ilam', 'Ilam'), ('Jhapa', 'Jhapa'), ('Khotang', 'Khotang'), ('Morang', 'Morang'), ('Okhaldhunga', 'Okhaldhunga'), ('Panchthar', 'Panchthar'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Solukhumbu', 'Solukhumbu'), ('Sunsari', 'Sunsari'), ('Taplejung', 'Taplejung'), ('Terhathum', 'Terhathum'), ('Udayapur', 'Udayapur'), ('Bara', 'Bara'), ('Dhanusha', 'Dhanusha'), ('Mahottari', 'Mahottari'), ('Parsa', 'Parsa'), ('Rautahat', 'Rautahat'), ('Saptari', 'Saptari'), ('Sarlahi', 'Sarlahi'), ('Siraha', 'Siraha'), ('Bhaktapur', 'Bhaktapur'), ('Chitwan', 'Chitwan'), ('Dhading', 'Dhading'), ('Dolakha', 'Dolakha'), ('Kathmandu', 'Kathmandu'), ('Kavrepalanchok', 'Kavrepalanchok'), ('Lalitpur', 'Lalitpur'), ('Makwanpur', 'Makwanpur'), ('Nuwakot', 'Nuwakot'), ('Ramechhap', 'Ramechhap'), ('Rasuwa', 'Rasuwa'), ('Sindhuli', 'Sindhuli'), ('Sindhupalchok', 'Sindhupalchok'), ('Baglung', 'Baglung'), ('Gorkha', 'Gorkha'), ('Kaski', 'Kaski'), ('Lamjung', 'Lamjung'), ('Manang', 'Manang'), ('Mustang', 'Mustang'), ('Myagdi', 'Myagdi'), ('Nawalpur', 'Nawalpur'), ('Parbat', 'Parbat'), ('Syangja', 'Syangja'), ('Tanahun', 'Tanahun'), ('Arghakhanchi', 'Arghakhanchi'), ('Banke', 'Banke'), ('Bardiya', 'Bardiya'), ('Dang', 'Dang'), ('Eastern Rukum', 'Eastern Rukum'), ('Gulmi', 'Gulmi'), ('Kapilvastu', 'Kapilvastu'), ('Parasi', 'Parasi'), ('Palpa', 'Palpa'), ('Pyuthan', 'Pyuthan'), ('Rolpa', 'Rolpa'), ('Rupandehi', 'Rupandehi'), ('Dailekh', 'Dailekh'), ('Dolpa', 'Dolpa'), ('Humla', 'Humla'), ('Jajarkot', 'Jajarkot'), ('Jumla', 'Jumla'), ('Kalikot', 'Kalikot'), ('Mugu', 'Mugu'), ('Salyan', 'Salyan'), ('Surkhet', 'Surkhet'), ('Western Rukum', 'Western Rukum'), ('Achham', 'Achham'), ('Baitadi', 'Baitadi'), ('Bajhang', 'Bajhang'), ('Bajura', 'Bajura'), ('Dadeldhura', 'Dadeldhura'), ('Darchula', 'Darchula'), ('Doti', 'Doti'), ('Kailali', 'Kailali'), ('Kanchanpur', 'Kanchanpur')], max_length=50)),
                ('local_unit_type', models.CharField(choices=[('Metropolitan', 'Metropolitan City'), ('Sub-Metropolitan', 'Sub-Metropolitan City'), ('Municipality', 'Municipality'), ('Rural Municipality', 'Rural Municipality')], max_length=20)),
                ('local_unit_name', models.CharField(max_length=50)),
                ('ward_no', models.PositiveIntegerField()),
                ('tole', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('passport', 'Passport'), ('student_citizenship', 'Student Citizenship'), ('parent_citizenship', 'Parent Citizenship'), ('plus_two_character', '+2 Character'), ('plus_two_transcript', '+2 Transcript'), ('tenth_character', '10th Character'), ('ward_recommendation', 'Ward Recommendation'), ('jlct', 'JLCT Certificate')], max_length=50)),
                ('verification_status', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('is_latest', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.UUID('dd4b0039-1e8a-4518-8248-3742de78748a'), editable=False, unique=True)),
                ('profile_pic', models.FileField(upload_to=admin_dashboard.models.profile_location, verbose_name='Profile Picture')),
                ('intake_month', models.CharField(blank=True, choices=[('january', 'January'), ('febuary', 'Febuary'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=20, null=True)),
                ('intake_year', models.CharField(blank=True, choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030')], max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('education_level', models.CharField(blank=True, choices=[('+2', '+2'), ('bachelor', 'Bachelor'), ('master', 'Master'), ('phd', 'PhD')], max_length=100, null=True)),
                ('notifications_enabled', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('', 'Select Status'), ('hold', 'Hold'), ('active', 'Active'), ('inactive', 'Inactive'), ('rejected', 'Rejected'), ('graduated', 'Graduated'), ('transferred', 'Transferred'), ('withdrawn', 'Withdrawn'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('permanent_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='permanent_address', to='admin_dashboard.address')),
                ('temporary_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temporary_address', to='admin_dashboard.address')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_detail', to='account.users')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=admin_dashboard.models.document_file_path)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='admin_dashboard.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='admin_dashboard.student'),
        ),
        migrations.AddField(
            model_name='document',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.users'),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('student', 'document_type', 'version')},
        ),
    ]
