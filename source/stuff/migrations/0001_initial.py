# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('location', models.TextField()),
                ('container', models.TextField()),
                ('description', models.TextField()),
                ('unit', models.TextField()),
                ('Qty', models.IntegerField()),
                ('purchaseDate', models.DateTimeField()),
                ('bestByDate', models.DateTimeField()),
                ('checkOnFrequency', models.TextField()),
                ('moreInfoLink', models.TextField()),
                ('waterStored', models.IntegerField()),
                ('numServings', models.IntegerField()),
                ('calPerServing', models.IntegerField()),
                ('prescriptionMed', models.BooleanField()),
            ],
        ),
    ]
