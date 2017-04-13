# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0009_auto_20170412_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='relycount',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default=b'static/article/Thumbnails/no-img.jpg', upload_to=b'static/article/Thumbnails/', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
