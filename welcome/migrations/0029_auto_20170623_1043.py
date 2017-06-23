# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0028_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='advertisers',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x95\x86', blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='position',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'top', '\u9876\u90e8'), (b'footer', '\u5e95\u90e8'), (b'left', '\u5de6\u8fb9'), (b'right', '\u53f3\u8fb9')]),
        ),
    ]
