# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150912_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.FileField(upload_to=b'carousel', verbose_name='\u8f6e\u64ad\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='clubintro',
            name='img',
            field=models.FileField(upload_to=b'Clubintropic', verbose_name='Club\u4ecb\u7ecd\u56fe\u7247'),
        ),
    ]
