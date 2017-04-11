# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_guestbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe8\x80\x85ip')),
                ('count', models.IntegerField(verbose_name=b'\xe8\xaf\xa5IP\xe8\xae\xbf\xe9\x97\xae\xe6\xac\xa1\xe6\x95\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe5\x85\xac\xe5\x91\x8a')),
                ('timemodify', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pageviews', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('isstick', models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\xa1\xb6\xe7\xbd\xae')),
                ('stickposition', models.IntegerField(verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6\xe4\xbd\x8d\xe7\xbd\xae')),
                ('timemodify', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('timemodify', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleRely',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85\xe5\x90\x8d\xe7\xa7\xb0')),
                ('email', models.CharField(default=None, max_length=80, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85\xe9\x82\xae\xe7\xae\xb1')),
                ('content', models.TextField(max_length=500, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('timemodify', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('artid', models.ForeignKey(related_name='artrely', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x96\x87\xe7\xab\xa0', to='welcome.Article')),
                ('commentid', models.ForeignKey(related_name='arirely', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8did', to='welcome.ArticleRely')),
                ('commentip', models.ForeignKey(related_name='comment', verbose_name=b'ip', to='welcome.ArticleRely')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='articale', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x88\xab', to='welcome.ArticleCategory'),
        ),
    ]
