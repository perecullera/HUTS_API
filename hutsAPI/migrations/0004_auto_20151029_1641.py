# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0003_auto_20151028_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='door',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='flat',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.IntegerField(null=True),
        ),
    ]
