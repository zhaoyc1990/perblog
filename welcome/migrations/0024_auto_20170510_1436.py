# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0023_share'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('timemodify', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5206\u4eab\u7c7b\u522b',
                'verbose_name_plural': '\u5206\u4eab\u7c7b\u522b',
            },
        ),
        migrations.AddField(
            model_name='share',
            name='categoryid',
            field=models.ForeignKey(related_name='category', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', blank=True, to='welcome.ShareCategory', null=True),
        ),
    ]
