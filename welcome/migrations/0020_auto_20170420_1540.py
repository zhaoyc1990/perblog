# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0019_auto_20170420_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerely',
            name='photo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='articlerely',
            name='email',
            field=models.CharField(max_length=80, null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
    ]
