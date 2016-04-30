# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150514_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='article',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0', to='blog.Article', null=True),
        ),
    ]
