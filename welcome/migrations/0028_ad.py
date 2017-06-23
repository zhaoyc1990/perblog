# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0027_auto_20170622_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', choices=[('\u9876\u90e8', b'top'), ('\u5e95\u90e8', b'footer'), ('\u5de6\u8fb9', b'left'), ('\u53f3\u8fb9', b'right')])),
                ('content', models.TextField(verbose_name=b'\xe4\xbb\xa3\xe7\xa0\x81\xef\xbc\x9a')),
            ],
            options={
                'verbose_name': '\u5e7f\u544a\u4ee3\u7801',
                'verbose_name_plural': '\u5e7f\u544a\u4ee3\u7801',
            },
        ),
    ]
