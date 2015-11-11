# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('debates', '0003_remove_debate_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 22, 3, 37, 928000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
