# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.IntegerField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('number', models.CharField(max_length=100, null=True, blank=True)),
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
                ('telefon', models.IntegerField(null=True)),
                ('bloc', models.CharField(max_length=10, blank=True)),
                ('flat', models.IntegerField(null=True)),
                ('door', models.IntegerField(null=True)),
                ('building', models.ForeignKey(related_name='hut', default=0, to='hutsAPI.Building')),
            ],
        ),
    ]
