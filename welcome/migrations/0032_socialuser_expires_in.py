# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0031_auto_20170628_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuser',
            name='expires_in',
            field=models.IntegerField(null=True, verbose_name=b'token\xe8\xbf\x87\xe6\x9c\x9f\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3', blank=True),
        ),
    ]
