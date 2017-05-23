# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='material',
            fields=[
                ('ID', models.AutoField(verbose_name='\u5e8f\u53f7', serialize=False, auto_created=True, primary_key=True)),
                ('material_name', models.CharField(max_length=120, verbose_name='\u6750\u6599')),
            ],
            options={
                'db_table': 'product_material',
                'verbose_name': '\u6750\u6599',
                'verbose_name_plural': '\u6750\u6599',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('ID', models.AutoField(verbose_name='\u5e8f\u53f7', serialize=False, auto_created=True, primary_key=True)),
                ('product_no', models.CharField(max_length=40, verbose_name='\u4ea7\u54c1\u7f16\u7801')),
                ('product_name', models.CharField(max_length=60, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('product_sale_name', models.CharField(max_length=60, null=True, verbose_name='\u4ea7\u54c1\u9500\u552e\u540d\u79f0')),
                ('product_instroduce', models.TextField(verbose_name='\u4ea7\u54c1\u7b80\u4ecb')),
            ],
            options={
                'db_table': 'product',
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('ID', models.AutoField(verbose_name='\u5e8f\u53f7', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=120, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('image_path', models.ImageField(upload_to=b'productimage/')),
            ],
            options={
                'db_table': 'product_image',
                'verbose_name': '\u4ea7\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u4ea7\u54c1\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='sequence',
            fields=[
                ('ID', models.AutoField(verbose_name='\u5e8f\u53f7', serialize=False, auto_created=True, primary_key=True)),
                ('sequence_name', models.CharField(max_length=100, verbose_name='\u7cfb\u5217')),
            ],
            options={
                'db_table': 'product_sequence',
                'verbose_name': '\u7cfb\u5217',
                'verbose_name_plural': '\u7cfb\u5217',
            },
        ),
        migrations.CreateModel(
            name='standard',
            fields=[
                ('ID', models.AutoField(verbose_name='\u5e8f\u53f7', serialize=False, auto_created=True, primary_key=True)),
                ('standard_name', models.CharField(max_length=100, verbose_name='\u6267\u884c\u6807\u51c6\u540d')),
                ('standard_no', models.CharField(max_length=255, verbose_name='\u6267\u884c\u6807\u51c6\u53f7')),
            ],
            options={
                'db_table': 'product_standard',
                'verbose_name': '\u6267\u884c\u6807\u51c6',
                'verbose_name_plural': '\u6267\u884c\u6807\u51c6',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_id',
            field=models.ManyToManyField(to='product.product_image', null=True, verbose_name='\u4ea7\u54c1\u56fe\u7247'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_material_id',
            field=models.ManyToManyField(to='product.material', verbose_name='\u4ea7\u54c1\u6750\u6599'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_sequence_id',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u7cfb\u5217', to='product.sequence'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_standard_id',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u6267\u884c\u6807\u51c6', to='product.standard'),
        ),
    ]
