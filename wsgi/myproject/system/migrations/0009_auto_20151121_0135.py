# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20151121_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='candidate_id',
            field=models.ManyToManyField(to='system.Candidate'),
        ),
    ]
