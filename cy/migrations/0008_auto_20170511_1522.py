# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0007_auto_20170511_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopinfo',
            name='mallType',
            field=models.CharField(max_length=3, null=True, verbose_name='\u5356\u573a\u7c7b\u578b', db_column=b'mallTyep'),
        ),
    ]
