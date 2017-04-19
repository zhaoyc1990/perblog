# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0016_auto_20170418_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='name',
            new_name='title',
        ),
    ]
