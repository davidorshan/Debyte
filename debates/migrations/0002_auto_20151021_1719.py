# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='allow_anon_users',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='debate',
            name='anon_username_joiner',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='debate',
            name='anon_username_starter',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='debate',
            name='joiner_user',
            field=models.ForeignKey(related_name='debate_joiner_user', default=None, blank=True, to='debates.User', null=True),
        ),
        migrations.AlterField(
            model_name='debate',
            name='starter_user',
            field=models.ForeignKey(related_name='debate_starter_user', default=None, blank=True, to='debates.User', null=True),
        ),
    ]
