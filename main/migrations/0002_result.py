# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mba', models.IntegerField(default=0)),
                ('mtech', models.IntegerField(default=0)),
                ('mbawe', models.IntegerField(default=0)),
                ('govt', models.IntegerField(default=0)),
                ('priv', models.IntegerField(default=0)),
                ('bank', models.IntegerField(default=0)),
                ('civil', models.IntegerField(default=0)),
                ('entre', models.IntegerField(default=0)),
                ('ms', models.IntegerField(default=0)),
            ],
        ),
    ]
