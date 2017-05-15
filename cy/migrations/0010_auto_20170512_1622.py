# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0009_auto_20170511_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinfo',
            name='shop_brand',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='\u54c1\u724c', db_column=b'shopbrand'),
        ),
        migrations.AlterField(
            model_name='datadiff',
            name='diff',
            field=models.TextField(null=True, verbose_name='\u5dee\u5f02\u539f\u56e0', blank=True),
        ),
    ]
