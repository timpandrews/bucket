# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0010_container'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='container',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stuff.Container'),
        ),
    ]
