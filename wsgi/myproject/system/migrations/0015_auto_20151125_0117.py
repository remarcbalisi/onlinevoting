# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0014_auto_20151123_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='first_name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='middle_name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='election',
            name='year',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(default=1, unique=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(default=1, unique=True, max_length=20),
            preserve_default=False,
        ),
    ]
