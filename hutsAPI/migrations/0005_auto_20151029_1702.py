# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0004_auto_20151029_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='hut',
        ),
        migrations.AddField(
            model_name='hut',
            name='door',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='flat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='postal_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
