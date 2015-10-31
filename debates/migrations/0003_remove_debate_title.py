# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debates', '0002_auto_20151021_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debate',
            name='title',
        ),
    ]
