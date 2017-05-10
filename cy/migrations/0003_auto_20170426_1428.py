# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0002_auto_20170401_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datadiff',
            options={'ordering': ['-date'], 'verbose_name': '\u5dee\u5f02\u8868', 'verbose_name_plural': '\u5dee\u5f02\u8868'},
        ),
        migrations.AlterField(
            model_name='datadiff',
            name='diff',
            field=models.TextField(default=b'\xe6\x97\xa0', null=True, verbose_name='\u5dee\u5f02\u539f\u56e0', blank=True),
        ),
        migrations.AlterField(
            model_name='datadiff',
            name='shop_amount',
            field=models.FloatField(default=0, null=True, verbose_name='\u4e0a\u62a5\u91d1\u989d', blank=True),
        ),
        migrations.AlterField(
            model_name='datadiff',
            name='sys_amount',
            field=models.FloatField(default=0, null=True, verbose_name='\u7cfb\u7edf\u91d1\u989d', blank=True),
        ),
    ]
