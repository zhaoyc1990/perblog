# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import welcome.models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0013_auto_20170413_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('link', models.CharField(max_length=100, verbose_name=b'\xe8\xb6\x85\xe8\xbf\x9e\xe6\x8e\xa5')),
            ],
            options={
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='protagonist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('photo', django_thumbs.db.models.ImageWithThumbsField(default=b'static/article/Thumbnails/no-img.jpg', upload_to=welcome.models.generate_filename)),
                ('sex', models.IntegerField(null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7')])),
                ('career', models.CharField(max_length=30, verbose_name=b'\xe8\x81\x8c\xe4\xb8\x9a')),
                ('location', models.CharField(help_text=b'\xe7\x9c\x81-\xe5\xb8\x82', max_length=100, verbose_name=b'\xe5\x9c\xb0\xe7\x90\x86\xe4\xbd\x8d\xe7\xbd\xae')),
                ('githubnum', models.CharField(max_length=100, null=True, verbose_name=b'github.com\xe5\xb8\x90\xe5\x8f\xb7', blank=True)),
                ('qqnum', models.CharField(max_length=20, null=True, verbose_name=b'QQ\xe5\xb8\x90\xe5\x8f\xb7', blank=True)),
                ('sinanum', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x96\xb0\xe6\xb5\xaa\xe5\xbe\xae\xe5\x8d\x9a\xe5\xb8\x90\xe5\x8f\xb7', blank=True)),
                ('twitter', models.CharField(max_length=50, null=True, verbose_name=b'twitter\xe5\xb8\x90\xe5\x8f\xb7', blank=True)),
                ('selfinfo', models.TextField(verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe4\xbb\x8b\xe7\xbb\x8d')),
            ],
            options={
                'verbose_name': '\u535a\u4e3b\u4fe1\u606f',
                'verbose_name_plural': '\u535a\u4e3b\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='websiteinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5title')),
                ('photo', django_thumbs.db.models.ImageWithThumbsField(upload_to=welcome.models.generate_filename)),
                ('casenum', models.CharField(help_text=b'\xe6\xb2\xa1\xe6\x9c\x89\xef\xbc\x8c\xe4\xb8\x8d\xe5\x86\x99', max_length=50, verbose_name=b'\xe5\xa4\x87\xe6\xa1\x88\xe5\x8f\xb7')),
                ('bottom', models.TextField(default=b'Copyright\xc2\xa92017\xe8\xb5\xb5\xe5\xbd\xa6\xe6\x98\x8c\xe5\x8d\x9a\xe5\xae\xa2Design By LY', verbose_name=b'\xe5\xba\x95\xe9\x83\xa8')),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u4fe1\u606f',
                'verbose_name_plural': '\u7f51\u7ad9\u4fe1\u606f',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': '\u6587\u7ae0\u7c7b\u522b', 'verbose_name_plural': '\u6587\u7ae0\u7c7b\u522b'},
        ),
        migrations.AlterModelOptions(
            name='articlerely',
            options={'verbose_name': '\u6587\u7ae0\u8bc4\u8bba\u53ca\u8bc4\u8bba\u56de\u590d', 'verbose_name_plural': '\u6587\u7ae0\u8bc4\u8bba\u53ca\u8bc4\u8bba\u56de\u590d'},
        ),
        migrations.AlterModelOptions(
            name='guestbook',
            options={'verbose_name': '\u7f51\u7ad9\u7559\u8a00', 'verbose_name_plural': '\u7f51\u7ad9\u7559\u8a00'},
        ),
        migrations.AlterModelOptions(
            name='timeline',
            options={'verbose_name': '\u65f6\u5149\u7ebf', 'verbose_name_plural': '\u65f6\u5149\u7ebf'},
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=django_thumbs.db.models.ImageWithThumbsField(default=b'static/article/Thumbnails/no-img.jpg', upload_to=welcome.models.generate_filename),
        ),
    ]
