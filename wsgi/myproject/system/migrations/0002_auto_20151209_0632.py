# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bulletin_info', models.CharField(max_length=300, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tally',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='firstname',
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
            model_name='position',
            name='slot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='college',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_voted',
            field=models.BooleanField(default=False),
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
        migrations.AddField(
            model_name='vote',
            name='date_time_voted',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='user_id',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=50, unique=True, null=True),
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
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(default=1, unique=True, max_length=20),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='candidate_id',
        ),
        migrations.AddField(
            model_name='vote',
            name='candidate_id',
            field=models.ManyToManyField(to='system.Candidate'),
        ),
        migrations.AddField(
            model_name='tally',
            name='candidate_id',
            field=models.ForeignKey(blank=True, to='system.Candidate', null=True),
        ),
        migrations.AddField(
            model_name='tally',
            name='election_id',
            field=models.ForeignKey(blank=True, to='system.Election', null=True),
        ),
    ]
