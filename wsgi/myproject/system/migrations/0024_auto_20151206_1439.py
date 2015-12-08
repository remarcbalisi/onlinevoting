# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0023_auto_20151203_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='candidate',
            name='achievements',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='life_quote',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='platform',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='user_id',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='college',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
