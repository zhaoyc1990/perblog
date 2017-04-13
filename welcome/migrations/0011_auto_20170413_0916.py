# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0010_auto_20170413_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlerely',
            name='commentid',
            field=models.ForeignKey(related_name='arirely', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8did', blank=True, to='welcome.ArticleRely', null=True),
        ),
        migrations.AlterField(
            model_name='articlerely',
            name='commentip',
            field=models.ForeignKey(related_name='artrely', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8dip', blank=True, to='welcome.AccessBy', null=True),
        ),
    ]
