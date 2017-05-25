# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170524_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='product_id',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1ID', to='product.product'),
        ),
    ]
