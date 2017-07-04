# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0035_auto_20170704_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerely',
            name='review',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xae\xa1\xe6\xa0\xb8\xe9\x80\x9a\xe8\xbf\x87'),
        ),
        migrations.AddField(
            model_name='guestbook',
            name='review',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xae\xa1\xe6\xa0\xb8\xe9\x80\x9a\xe8\xbf\x87'),
        ),
    ]
