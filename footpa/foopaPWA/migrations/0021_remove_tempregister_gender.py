# Generated by Django 3.0.2 on 2020-01-30 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0020_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempregister',
            name='gender',
        ),
    ]
