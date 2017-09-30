# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0012_auto_20170515_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadiff',
            name='remark',
            field=models.TextField(default='\u672a\u6838\u67e5', null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='datadiff',
            name='true_amount',
            field=models.IntegerField(default=2, verbose_name='\u6b63\u786e\u503c', db_column=b'true_amount'),
        ),
    ]
