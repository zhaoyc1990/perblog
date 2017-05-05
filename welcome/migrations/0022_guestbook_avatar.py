# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0021_auto_20170505_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='avatar',
            field=models.CharField(default=b'/static/images/Logo_40.png', max_length=200, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
