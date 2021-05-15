# Generated by Django 2.2 on 2021-05-15 21:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_auto_20210515_1938'),
    ]
    atomic = False
    operations = [
        migrations.AddField(
            model_name='trips',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trips',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
