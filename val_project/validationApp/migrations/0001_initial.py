# Generated by Django 4.2.7 on 2023-12-19 08:35

import django.core.validators
from django.db import migrations, models
import validationApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(validators=[validationApp.models.validate_date_of_birth])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(message='Email must be from UR (ur.ac.rw)', regex='@ur\\.ac\\.rw$')])),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must start with + country code', regex='^\\+\\d{1,4}-\\d{1,15}$')])),
                ('reference_number', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Reference number must be between 99 and 999', regex='^[1-9]\\d{1,2}$')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
            ],
        ),
    ]
