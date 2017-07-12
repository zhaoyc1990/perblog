# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0038_auto_20170707_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerely',
            name='emailsend',
            field=models.BooleanField(default=False, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe9\x80\x81\xe6\x88\x90\xe5\x8a\x9f'),
        ),
        migrations.AddField(
            model_name='guestbook',
            name='emailsend',
            field=models.BooleanField(default=False, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe9\x80\x81\xe6\x88\x90\xe5\x8a\x9f'),
        ),
    ]
