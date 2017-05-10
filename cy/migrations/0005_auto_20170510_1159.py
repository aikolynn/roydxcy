# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0004_auto_20170510_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, db_column=b'id', serialize=False, verbose_name='\u533a\u57dfID'),
        ),
    ]
