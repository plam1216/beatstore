# Generated by Django 4.1.2 on 2022-10-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_rename_coverart_beat_cover_art_rename_ig_producer_ig_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beat',
            old_name='cover_art',
            new_name='audio',
        ),
        migrations.AddField(
            model_name='beat',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]