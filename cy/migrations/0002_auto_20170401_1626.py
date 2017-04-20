# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopinfo',
            name='shopType',
            field=models.CharField(max_length=2, verbose_name='\u7ecf\u8425\u65b9\u5f0f', db_column=b'shopType', choices=[(b'D', '\u76f4\u8425'), (b'A', '\u4ee3\u7406'), (b'J', '\u52a0\u76df'), (b'C', '\u627f\u5305')]),
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='state',
            field=models.CharField(max_length=2, verbose_name='\u8fd0\u8425\u72b6\u6001', db_column=b'state', choices=[(b'S', '\u6b63\u5e38\u8425\u4e1a'), (b'Z', '\u88c5\u4fee'), (b'C', '\u64a4\u5e97'), (b'P', '\u6682\u505c\u6574\u6539')]),
        ),
    ]
