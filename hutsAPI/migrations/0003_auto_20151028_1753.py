# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0002_auto_20151028_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hut',
            name='telefon',
            field=models.IntegerField(null=True),
        ),
    ]
