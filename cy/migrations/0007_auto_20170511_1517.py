# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0006_auto_20170510_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopinfo',
            name='contractBeginDate',
            field=models.DateField(null=True, verbose_name='\u5408\u540c\u5f00\u59cb\u65f6\u95f4', db_column=b'contractBeginDate'),
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='contractEndDate',
            field=models.DateField(null=True, verbose_name='\u5408\u540c\u7ed3\u675f\u65f6\u95f4', db_column=b'contractEndDate'),
        ),
    ]
