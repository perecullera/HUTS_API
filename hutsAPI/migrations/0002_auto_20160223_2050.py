# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hut',
            name='bloc',
        ),
        migrations.AddField(
            model_name='building',
            name='bloc',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
