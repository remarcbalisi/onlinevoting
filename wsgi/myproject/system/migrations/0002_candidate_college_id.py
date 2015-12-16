# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='college_id',
            field=models.ForeignKey(blank=True, to='system.College', null=True),
        ),
    ]
