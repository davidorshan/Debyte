# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('timestamp', models.DateTimeField()),
                ('message', models.CharField(max_length=500, serialize=False, primary_key=True)),
                ('chatroom_id', models.ForeignKey(to='chat.Chatroom')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(to='debates.User'),
        ),
    ]
