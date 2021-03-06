# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150907_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubIntro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('img', models.FileField(upload_to=b'./static/Clubintropic/', verbose_name='Club\u4ecb\u7ecd\u56fe\u7247')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': 'club\u4ecb\u7ecd\u56fe\u7247',
                'verbose_name_plural': 'club\u4ecb\u7ecd\u56fe\u7247',
            },
        ),
    ]
