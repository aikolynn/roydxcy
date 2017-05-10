# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0003_auto_20170426_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='company_cellphone',
            field=models.CharField(max_length=11, null=True, verbose_name='\u516c\u53f8\u624b\u673a'),
        ),
    ]
