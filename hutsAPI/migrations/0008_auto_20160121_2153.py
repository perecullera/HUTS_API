# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hutsAPI', '0007_auto_20160121_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='postal_code',
            new_name='zip',
        ),
    ]
