# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadiff',
            name='true_amount',
            field=models.FloatField(default=models.FloatField(default=0, null=True, verbose_name='\u4e0a\u62a5\u91d1\u989d', blank=True), verbose_name='\u6b63\u786e\u503c', db_column=b'true_amount'),
        ),
    ]
