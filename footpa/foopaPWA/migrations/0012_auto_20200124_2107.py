# Generated by Django 3.0.2 on 2020-01-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0011_auto_20200124_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='id',
        ),
        migrations.AlterField(
            model_name='match',
            name='match_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
