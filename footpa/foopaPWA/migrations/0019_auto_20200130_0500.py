# Generated by Django 3.0.2 on 2020-01-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0018_tempregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempregister',
            name='id',
        ),
        migrations.AlterField(
            model_name='tempregister',
            name='register_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tempregister',
            name='register_time_expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tempregister',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]