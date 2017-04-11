# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_auto_20170411_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.CharField(default=b'null', max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
