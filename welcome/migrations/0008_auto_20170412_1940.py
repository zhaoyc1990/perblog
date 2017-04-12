# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_auto_20170412_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=120, null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default=b'static/article/Thumbnails/no-img.jpg', upload_to=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
