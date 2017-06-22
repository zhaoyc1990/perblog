# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import welcome.models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0026_share_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteinfo',
            name='websiteip',
            field=models.CharField(default=b'#', max_length=200, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe9\xa6\x96\xe9\xa1\xb5\xe5\x9f\x9f\xe5\x90\x8d(www.zhaoyanchang.com)'),
        ),
        migrations.AlterField(
            model_name='share',
            name='img',
            field=django_thumbs.db.models.ImageWithThumbsField(default=b'/static/article/Thumbnails/no-img.jpg', upload_to=welcome.models.generate_filename),
        ),
        migrations.AlterField(
            model_name='share',
            name='webimg',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe5\x9b\xbe\xe7\x89\x87\xe7\x94\xa8\xe4\xba\x8e\xe6\x96\x87\xe7\xab\xa0\xe5\x8f\xaf\xe8\xa7\x82\xe6\x80\xa7\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
