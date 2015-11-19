# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='year',
            field=models.IntegerField(unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(max_length=20, unique=True, null=True),
        ),
    ]
