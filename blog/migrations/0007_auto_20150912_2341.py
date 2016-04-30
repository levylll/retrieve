# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_clubintro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontpic',
            name='img',
            field=models.FileField(upload_to=b'frontpic', verbose_name='\u9996\u9875\u56fe\u7247'),
        ),
    ]
