# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0024_auto_20170510_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='show',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe6\xbc\x94\xe7\xa4\xba\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
