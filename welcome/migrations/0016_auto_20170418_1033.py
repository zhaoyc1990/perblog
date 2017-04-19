# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0015_auto_20170418_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteinfo',
            name='casenum',
            field=models.CharField(help_text=b'\xe6\xb2\xa1\xe6\x9c\x89\xef\xbc\x8c\xe4\xb8\x8d\xe5\x86\x99', max_length=50, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xa1\x88\xe5\x8f\xb7', blank=True),
        ),
    ]
