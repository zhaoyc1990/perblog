# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0036_auto_20170704_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smtpmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(max_length=50, verbose_name=b'STMP\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x9f\x9f\xe5\x90\x8d:')),
                ('port', models.IntegerField(verbose_name=b'STMP\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xab\xaf\xe5\x8f\xa3:')),
                ('user', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d:')),
                ('password', models.CharField(max_length=100, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\xaf\x86\xe7\xa0\x81:')),
                ('tls', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x9c\x80\xe8\xa6\x81\xe5\xbc\x80\xe5\x90\xaftls')),
                ('enabled', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8\xe8\xaf\xa5\xe9\x82\xae\xe7\xae\xb1')),
            ],
            options={
                'verbose_name': '\u53d1\u9001\u90ae\u7bb1\u670d\u52a1\u5668\u914d\u7f6e',
                'verbose_name_plural': '\u53d1\u9001\u90ae\u7bb1\u670d\u52a1\u5668\u914d\u7f6e',
            },
        ),
    ]
