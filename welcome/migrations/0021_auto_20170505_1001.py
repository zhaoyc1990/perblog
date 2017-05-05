# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0020_auto_20170420_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessby',
            options={'verbose_name': 'IP\u8bb0\u5f55', 'verbose_name_plural': 'IP\u8bb0\u5f55'},
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'verbose_name': '\u7f51\u7ad9\u516c\u544a', 'verbose_name_plural': '\u7f51\u7ad9\u516c\u544a'},
        ),
        migrations.AlterModelOptions(
            name='pageview',
            options={'verbose_name': '\u6ca1\u7528', 'verbose_name_plural': '\u6ca1\u7528'},
        ),
        migrations.AddField(
            model_name='guestbook',
            name='messagerely',
            field=models.ForeignKey(related_name='relymessage', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8did', blank=True, to='welcome.GuestBook', null=True),
        ),
        migrations.AddField(
            model_name='guestbook',
            name='website',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
