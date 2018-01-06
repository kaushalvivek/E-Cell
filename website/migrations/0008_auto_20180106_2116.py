# Generated by Django 2.0.1 on 2018-01-06 21:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_merge_20180106_1845'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GalleryManager',
        ),
        migrations.AlterModelManagers(
            name='album',
            managers=[
                ('all_albums', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='pictures',
            managers=[
                ('pics', django.db.models.manager.Manager()),
            ],
        ),
    ]