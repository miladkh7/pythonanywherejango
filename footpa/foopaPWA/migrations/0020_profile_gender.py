# Generated by Django 3.0.2 on 2020-01-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0019_auto_20200130_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=5, null=True),
        ),
    ]