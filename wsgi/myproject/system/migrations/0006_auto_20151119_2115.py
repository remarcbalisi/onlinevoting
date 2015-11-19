# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20151119_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='college_id',
            field=models.ForeignKey(blank=True, to='system.College', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_id',
            field=models.ForeignKey(blank=True, to='system.Party', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='position_id',
            field=models.ForeignKey(blank=True, to='system.Position', null=True),
        ),
    ]
