# Generated by Django 4.1.2 on 2022-10-21 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_beat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='producers',
        ),
    ]
