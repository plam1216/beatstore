# Generated by Django 4.1.2 on 2022-10-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_beat_coverart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='coverart',
            field=models.FileField(upload_to=''),
        ),
    ]
