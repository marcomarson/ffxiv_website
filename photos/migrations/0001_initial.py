# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field='height', upload_to='', width_field='width')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
