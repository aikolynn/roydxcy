# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0005_auto_20170510_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadiff',
            name='id',
            field=models.AutoField(verbose_name='\u8d26\u76eeID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='id',
            field=models.AutoField(verbose_name='\u7528\u6237ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='Id',
            field=models.AutoField(auto_created=True, primary_key=True, db_column=b'Id', serialize=False, verbose_name='\u5e97\u94faID'),
        ),
    ]
