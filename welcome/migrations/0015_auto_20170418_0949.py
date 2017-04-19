# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0014_auto_20170418_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteinfo',
            name='info',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='websiteinfo',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
