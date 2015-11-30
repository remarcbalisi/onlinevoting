# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
    ]
