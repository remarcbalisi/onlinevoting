# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0020_auto_20151202_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='course',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='year',
        ),
        migrations.AlterField(
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
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
    ]
