# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0024_auto_20151206_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='college_id',
        ),
    ]
