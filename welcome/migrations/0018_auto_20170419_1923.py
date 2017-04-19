# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0017_auto_20170418_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='webimg',
            field=models.CharField(default=b'/static/article/Thumbnails/no-img.jpg', max_length=200, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe5\x9b\xbe\xe7\x89\x87\xe7\x94\xa8\xe4\xba\x8e\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AddField(
            model_name='protagonist',
            name='webimg',
            field=models.CharField(default=b'/static/article/Thumbnails/no-img.jpg', max_length=200, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe5\x9b\xbe\xe7\x89\x87\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
