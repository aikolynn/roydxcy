# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image_id',
        ),
        migrations.AddField(
            model_name='product_image',
            name='product_id',
            field=models.ForeignKey(default=None, verbose_name='\u4ea7\u54c1ID', to='product.product'),
        ),
    ]
