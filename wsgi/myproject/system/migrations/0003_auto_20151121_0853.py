# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20151118_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='firstname',
        ),
        migrations.AddField(
            model_name='candidate',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='middle_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
