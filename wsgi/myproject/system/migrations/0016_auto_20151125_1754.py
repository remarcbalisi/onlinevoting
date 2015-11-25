# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0015_auto_20151125_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_voted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vote',
            name='date_time_voted',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
