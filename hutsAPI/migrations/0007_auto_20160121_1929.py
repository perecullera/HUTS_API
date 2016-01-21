# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0006_auto_20151029_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postal_code', models.IntegerField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('number', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hut',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='hut',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='hut',
            name='number',
        ),
        migrations.RemoveField(
            model_name='hut',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='hut',
            name='street',
        ),
        migrations.AddField(
            model_name='hut',
            name='building',
            field=models.ForeignKey(related_name='hut', default=0, to='hutsAPI.Building'),
        ),
    ]
