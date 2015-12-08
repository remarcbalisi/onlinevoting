# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_auto_20151130_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='middle_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
    ]
