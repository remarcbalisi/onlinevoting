# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0022_auto_20151203_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
