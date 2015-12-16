# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id_number', models.CharField(unique=True, max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('address', models.CharField(max_length=30, null=True, blank=True)),
                ('course', models.CharField(max_length=30, null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('contact_number', models.CharField(max_length=30, null=True, blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_voted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bulletin_info', models.CharField(max_length=300, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.TextField(null=True, blank=True)),
                ('achievements', models.TextField(null=True, blank=True)),
                ('life_quote', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college_name', models.CharField(max_length=50, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('party_name', models.CharField(max_length=50, null=True)),
                ('election_id', models.ForeignKey(blank=True, to='system.Election', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position_name', models.CharField(unique=True, max_length=20)),
                ('slot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tally',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_count', models.IntegerField()),
                ('candidate_id', models.ForeignKey(blank=True, to='system.Candidate', null=True)),
                ('election_id', models.ForeignKey(blank=True, to='system.Election', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_voted', models.DateTimeField(null=True, blank=True)),
                ('candidate_id', models.ManyToManyField(to='system.Candidate')),
                ('election_id', models.ForeignKey(blank=True, to='system.Election', null=True)),
                ('user_id', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='election_id',
            field=models.ForeignKey(blank=True, to='system.Election', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_id',
            field=models.ForeignKey(blank=True, to='system.Party', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='position_id',
            field=models.ForeignKey(blank=True, to='system.Position', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='user_id',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='college_id',
            field=models.ForeignKey(blank=True, to='system.College', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
