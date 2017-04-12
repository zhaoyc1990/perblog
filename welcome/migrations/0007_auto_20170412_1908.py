# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_auto_20170411_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default=b'static/article/Thumbnails/no-img.jpg', upload_to=b'static/article/Thumbnails', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pageviews',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='stickposition',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
    ]
