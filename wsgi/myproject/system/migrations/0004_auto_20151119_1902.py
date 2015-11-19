# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='firstname',
            new_name='first_name',
        ),
    ]
