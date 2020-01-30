# Generated by Django 3.0.2 on 2020-01-30 01:30

from django.db import migrations, models
import foopaPWA.otherfunction


class Migration(migrations.Migration):

    dependencies = [
        ('foopaPWA', '0016_match_match_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_length',
            field=models.PositiveIntegerField(default=90, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_time',
            field=models.TimeField(default=foopaPWA.otherfunction.default_start_time),
        ),
    ]