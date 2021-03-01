# Generated by Django 3.1.6 on 2021-03-01 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0004_auto_20210301_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 05999999999', regex='^[0-9]*$')]),
        ),
    ]
