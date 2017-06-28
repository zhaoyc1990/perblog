# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0030_socialaccount_socialuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialaccount',
            options={'verbose_name': '\u793e\u4ea4\u767b\u9646\u4e92\u8054', 'verbose_name_plural': '\u793e\u4ea4\u767b\u9646\u4e92\u8054'},
        ),
        migrations.AlterModelOptions(
            name='socialuser',
            options={'verbose_name': '\u793e\u4ea4\u767b\u9646\u4e92\u8054\u7528\u6237', 'verbose_name_plural': '\u793e\u4ea4\u767b\u9646\u4e92\u8054\u7528\u6237'},
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='code_url',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8e\xb7\xe5\x8f\x96Authorization Code url', blank=True),
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='token_url',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8e\xb7\xe5\x8f\x96Access Token url', blank=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='sex',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7')]),
        ),
    ]
