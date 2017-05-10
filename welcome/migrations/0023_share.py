# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import welcome.models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0022_guestbook_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('tags', models.CharField(max_length=120, null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe', blank=True)),
                ('abstract', models.CharField(max_length=300, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True)),
                ('content', models.TextField(default=None, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('img', django_thumbs.db.models.ImageWithThumbsField(default=b'static/article/Thumbnails/no-img.jpg', upload_to=welcome.models.generate_filename)),
                ('webimg', models.CharField(default=b'/static/article/Thumbnails/no-img.jpg', max_length=200, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe5\x9b\xbe\xe7\x89\x87\xe7\x94\xa8\xe4\xba\x8e\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87')),
                ('pageviews', models.IntegerField(default=0, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0')),
                ('relycount', models.PositiveIntegerField(default=0, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe9\x87\x8f')),
                ('isstick', models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\xa1\xb6\xe7\xbd\xae')),
                ('stickposition', models.IntegerField(default=0, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6\xe4\xbd\x8d\xe7\xbd\xae')),
                ('timemodify', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5206\u4eab',
                'verbose_name_plural': '\u5206\u4eab',
            },
        ),
    ]
