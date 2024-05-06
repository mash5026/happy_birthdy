# Generated by Django 5.0.4 on 2024-04-29 06:59

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdayMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_of_birth', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', django_jalali.db.models.jDateField()),
                ('activity_unit', models.CharField(max_length=100)),
                ('specilization', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=12)),
            ],
        ),
    ]
