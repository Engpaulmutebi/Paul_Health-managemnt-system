# Generated by Django 5.1.3 on 2024-11-07 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='images')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Appointment_Scheduled', 'Appointment_Scheduled'), ('Appointment_Cancelled', 'Appointment_Cancelled')], max_length=100)),
                ('seen', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'Notification',
            },
        ),
    ]
