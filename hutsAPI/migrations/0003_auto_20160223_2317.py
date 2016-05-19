# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0002_auto_20160223_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hut',
            name='door',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hut',
            name='flat',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
