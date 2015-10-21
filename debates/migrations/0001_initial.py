# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('numberMessage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('orig_position', models.CharField(max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('anon_username_starter', models.CharField(max_length=100)),
                ('anon_username_joiner', models.CharField(max_length=100)),
                ('allow_anon_users', models.BooleanField(max_length=100)),
                ('category', models.ForeignKey(to='debates.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='debate',
            name='joiner_user',
            field=models.ForeignKey(related_name='debate_joiner_user', to='debates.User'),
        ),
        migrations.AddField(
            model_name='debate',
            name='starter_user',
            field=models.ForeignKey(related_name='debate_starter_user', to='debates.User'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='debate',
            field=models.ForeignKey(to='debates.Debate'),
        ),
    ]
