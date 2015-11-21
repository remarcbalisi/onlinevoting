# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20151121_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='candidate_id',
        ),
        migrations.AddField(
            model_name='vote',
            name='candidate_id',
            field=models.ForeignKey(blank=True, to='system.Candidate', null=True),
        ),
    ]
