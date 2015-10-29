# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0005_auto_20151029_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hut',
            name='number',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hut',
            name='street',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
