# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0037_smtpmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlerely',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
