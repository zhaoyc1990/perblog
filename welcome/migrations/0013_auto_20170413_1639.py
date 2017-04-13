# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0012_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='month',
            field=models.PositiveIntegerField(null=True, verbose_name=b'\xe6\x9c\x88', blank=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='year',
            field=models.PositiveIntegerField(null=True, verbose_name=b'\xe5\xb9\xb4', blank=True),
        ),
    ]
