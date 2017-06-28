# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0033_auto_20170628_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuser',
            name='city',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82', blank=True),
        ),
        migrations.AddField(
            model_name='socialuser',
            name='qqopenid',
            field=models.CharField(max_length=100, null=True, verbose_name=b'qq\xe5\x94\xaf\xe4\xb8\x80\xe6\xa0\x87\xe8\xaf\x86', blank=True),
        ),
    ]
