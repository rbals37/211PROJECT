# Generated by Django 5.1.2 on 2024-11-02 08:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=11),
            preserve_default=False,
        ),
    ]
