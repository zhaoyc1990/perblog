# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0032_socialuser_expires_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='sex',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7')]),
        ),
    ]
