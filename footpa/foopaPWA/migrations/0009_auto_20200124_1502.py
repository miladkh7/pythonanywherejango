# Generated by Django 3.0.2 on 2020-01-24 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0008_remove_user_user_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Token',
        ),
    ]
