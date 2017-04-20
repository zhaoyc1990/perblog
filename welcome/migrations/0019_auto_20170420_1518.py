# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0018_auto_20170419_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlerely',
            name='artid',
            field=models.ForeignKey(related_name='artrely', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x96\x87\xe7\xab\xa0', blank=True, to='welcome.Article', null=True),
        ),
    ]
