# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20151121_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='candidate_id',
        ),
        migrations.AddField(
            model_name='vote',
            name='candidate_id',
            field=models.ManyToManyField(to='system.Candidate', null=True, blank=True),
        ),
    ]