# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0025_share_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='download',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
