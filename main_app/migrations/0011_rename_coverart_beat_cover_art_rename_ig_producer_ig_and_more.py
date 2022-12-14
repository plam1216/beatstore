# Generated by Django 4.1.2 on 2022-10-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_beat_coverart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beat',
            old_name='coverart',
            new_name='cover_art',
        ),
        migrations.RenameField(
            model_name='producer',
            old_name='ig',
            new_name='IG',
        ),
        migrations.AddField(
            model_name='beat',
            name='bpm',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
