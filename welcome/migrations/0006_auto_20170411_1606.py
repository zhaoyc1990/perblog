# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_article_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='title',
        ),
    ]
