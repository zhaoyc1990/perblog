# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_auto_20170412_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(max_length=300, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0'),
        ),
    ]
