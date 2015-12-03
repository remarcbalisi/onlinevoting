# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0018_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bulletin_info', models.CharField(max_length=300, unique=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
    ]
