# Generated by Django 3.0.2 on 2020-01-20 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0003_auto_20200120_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]