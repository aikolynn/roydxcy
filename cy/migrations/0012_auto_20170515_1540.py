# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0011_datadiff_true_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadiff',
            name='true_amount',
            field=models.IntegerField(default=3, verbose_name='\u6b63\u786e\u503c', db_column=b'true_amount'),
        ),
    ]
