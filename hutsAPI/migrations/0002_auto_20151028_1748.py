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
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='hut',
            field=models.ForeignKey(default=None, to='hutsAPI.Hut'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hut',
            name='telefon',
            field=models.IntegerField(default=None, blank=True),
            preserve_default=False,
        ),
    ]
