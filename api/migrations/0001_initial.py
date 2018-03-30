# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-29 19:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField(default=2018, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2018)])),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('alias', models.CharField(help_text='May contain several values separated by comma.', max_length=255)),
                ('as_actor', models.ManyToManyField(blank=True, related_name='as_actor', to='api.Film')),
                ('as_director', models.ManyToManyField(blank=True, related_name='as_director', to='api.Film')),
                ('as_producer', models.ManyToManyField(blank=True, related_name='as_producer', to='api.Film')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]