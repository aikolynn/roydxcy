# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0010_auto_20170512_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='datadiff',
            name='true_amount',
            field=models.BooleanField(default=False, verbose_name='\u6b63\u786e\u503c', db_column=b'true_amount'),
        ),
    ]
