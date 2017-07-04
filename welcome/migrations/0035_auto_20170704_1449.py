# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0034_auto_20170628_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerely',
            name='socialuser',
            field=models.ForeignKey(related_name='relyuser', verbose_name=b'\xe7\xa4\xbe\xe4\xba\xa4\xe7\x94\xa8\xe6\x88\xb7', blank=True, to='welcome.Socialuser', null=True),
        ),
        migrations.AddField(
            model_name='articlerely',
            name='website',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85\xe7\xbd\x91\xe7\xab\x99', blank=True),
        ),
    ]
