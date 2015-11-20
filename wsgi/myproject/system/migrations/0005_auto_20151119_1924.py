# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20151119_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='party_id',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='position_id',
        ),
    ]
