# Generated by Django 3.0.2 on 2020-01-24 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foopaPWA', '0012_auto_20200124_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('matchcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foopaPWA.Match')),
                ('reciver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itemtwo', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itemone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
