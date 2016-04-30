# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmaig_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmaiguser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='vmaiguser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='vmaiguser',
            name='password',
            field=models.CharField(help_text="Don't do anything here!!!Don't do anything here!!!Don't do anything here!!!", max_length=128, verbose_name='password'),
        ),
    ]
