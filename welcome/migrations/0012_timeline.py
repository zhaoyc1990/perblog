# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0011_auto_20170413_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveIntegerField(verbose_name=b'\xe5\xb9\xb4')),
                ('month', models.PositiveIntegerField(verbose_name=b'\xe6\x9c\x88')),
                ('content', models.CharField(max_length=200, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
