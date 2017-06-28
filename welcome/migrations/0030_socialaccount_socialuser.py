# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import welcome.models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0029_auto_20170623_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socialaccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50, verbose_name=b'\xe8\xbd\xaf\xe4\xbb\xb6\xe5\x8e\x82\xe5\x95\x86(\xe5\x90\x8d\xe7\xa7\xb0)', choices=[(b'qq', b'QQ')])),
                ('appid', models.CharField(max_length=100, verbose_name=b'appid')),
                ('appkey', models.CharField(max_length=100, verbose_name=b'appkey')),
                ('redirect_url', models.CharField(max_length=100, verbose_name=b'\xe5\x9b\x9e\xe8\xb0\x83\xe5\x9c\xb0\xe5\x9d\x80')),
                ('code_url', models.CharField(max_length=100, verbose_name=b'\xe8\x8e\xb7\xe5\x8f\x96Authorization Code url')),
                ('token_url', models.CharField(max_length=100, verbose_name=b'\xe8\x8e\xb7\xe5\x8f\x96Access Token url')),
            ],
        ),
        migrations.CreateModel(
            name='Socialuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0', blank=True)),
                ('password', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81', blank=True)),
                ('website', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe7\xbd\x91\xe5\x9d\x80', blank=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('sex', models.IntegerField(verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7')], default=1)),
                ('photo', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('uploadphoto', django_thumbs.db.models.ImageWithThumbsField(default=b'static/article/Thumbnails/no-img.jpg', null=True, upload_to=welcome.models.generate_filename, blank=True)),
                ('access_token', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xaeaccess_token', blank=True)),
                ('refresh_token', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x87\xaa\xe5\x8a\xa8\xe7\xbb\xad\xe6\x9c\x9ftoken', blank=True)),
                ('qq', models.CharField(max_length=14, null=True, verbose_name=b'QQ\xe5\x8f\xb7', blank=True)),
                ('weibo', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a\xe5\x8f\xb7', blank=True)),
                ('github', models.CharField(max_length=100, null=True, verbose_name=b'github\xe5\xb8\x90\xe5\x8f\xb7', blank=True)),
                ('social', models.ForeignKey(related_name='user', verbose_name=b'\xe7\xa4\xbe\xe4\xba\xa4\xe5\x8e\x82\xe5\x95\x86', blank=True, to='welcome.Socialaccount', null=True)),
            ],
        ),
    ]
