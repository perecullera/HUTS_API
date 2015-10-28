# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('flat', models.IntegerField()),
                ('door', models.IntegerField()),
                ('postal_code', models.IntegerField()),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30)),
                ('DC', models.IntegerField()),
                ('name', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('address', models.ForeignKey(to='hutsAPI.Address')),
            ],
        ),
    ]
