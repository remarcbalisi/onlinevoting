# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0016_auto_20151125_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='slot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
