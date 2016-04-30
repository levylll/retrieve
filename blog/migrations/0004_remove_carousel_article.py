# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150907_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='article',
        ),
    ]
