# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='picUrl',
        ),
        migrations.AddField(
            model_name='person',
            name='fb',
            field=models.CharField(default='facebook.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='linkedin',
            field=models.CharField(default='linkedin.com', max_length=255),
            preserve_default=False,
        ),
    ]
