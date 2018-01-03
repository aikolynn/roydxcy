# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, db_column=b'id', serialize=False, verbose_name='\u533a\u57dfID')),
                ('name', models.CharField(max_length=40, verbose_name='\u533a\u57df\u540d\u79f0', db_column=b'name')),
            ],
            options={
                'db_table': 'area',
                'verbose_name': '\u533a\u57df\u4fe1\u606f',
                'verbose_name_plural': '\u533a\u57df\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='datadiff',
            fields=[
                ('id', models.AutoField(verbose_name='\u8d26\u76eeID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, verbose_name='\u65e5\u671f', blank=True)),
                ('shop_amount', models.FloatField(default=0, null=True, verbose_name='\u4e0a\u62a5\u91d1\u989d', blank=True)),
                ('sys_amount', models.FloatField(default=0, null=True, verbose_name='\u7cfb\u7edf\u91d1\u989d', blank=True)),
                ('amount', models.FloatField(default=0, null=True, verbose_name='\u5dee\u5f02\u91d1\u989d', blank=True)),
                ('diff', models.TextField(null=True, verbose_name='\u5dee\u5f02\u539f\u56e0', blank=True)),
                ('remark', models.TextField(default='\u672a\u6838\u67e5', null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('true_amount', models.IntegerField(default=2, verbose_name='\u6b63\u786e\u503c', db_column=b'true_amount')),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'datadiff',
                'verbose_name': '\u5dee\u5f02\u8868',
                'verbose_name_plural': '\u5dee\u5f02\u8868',
            },
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(verbose_name='\u7528\u6237ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u59d3\u540d')),
                ('personal_cellphone', models.CharField(max_length=11, verbose_name='\u79c1\u4eba\u624b\u673a')),
                ('company_cellphone', models.CharField(max_length=11, null=True, verbose_name='\u516c\u53f8\u624b\u673a')),
                ('qq', models.CharField(max_length=20, null=True, verbose_name='QQ', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('title', models.CharField(max_length=40, verbose_name='\u804c\u52a1')),
                ('address', models.CharField(max_length=255, verbose_name='\u901a\u8baf\u5730\u5740')),
            ],
            options={
                'db_table': 'Managers',
                'verbose_name': '\u533a\u57df\u7ba1\u7406\u4eba\u5458\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u533a\u57df\u7ba1\u7406\u4eba\u5458\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('Id', models.AutoField(auto_created=True, primary_key=True, db_column=b'Id', serialize=False, verbose_name='\u5e97\u94faID')),
                ('sName', models.CharField(max_length=255, null=True, verbose_name='\u5e97\u94fa\u540d\u79f0', db_column=b'sName', blank=True)),
                ('sysName', models.CharField(max_length=255, null=True, verbose_name='\u7cfb\u7edf\u540d\u79f0', db_column=b'sysName', blank=True)),
                ('state', models.CharField(max_length=2, verbose_name='\u8fd0\u8425\u72b6\u6001', db_column=b'state', choices=[(b'S', '\u6b63\u5e38\u8425\u4e1a'), (b'Z', '\u88c5\u4fee'), (b'C', '\u64a4\u5e97'), (b'P', '\u6682\u505c\u6574\u6539')])),
                ('mallType', models.CharField(max_length=3, null=True, verbose_name='\u5356\u573a\u7c7b\u578b', db_column=b'mallTyep')),
                ('shopType', models.CharField(max_length=2, verbose_name='\u7ecf\u8425\u65b9\u5f0f', db_column=b'shopType', choices=[(b'D', '\u76f4\u8425'), (b'A', '\u4ee3\u7406'), (b'J', '\u52a0\u76df'), (b'C', '\u627f\u5305')])),
                ('shopAddress', models.CharField(max_length=255, verbose_name='\u5e97\u94fa\u5730\u5740', db_column=b'shopAddress')),
                ('openingDate', models.DateField(default=None, verbose_name='\u5f00\u4e1a\u65f6\u95f4', db_column=b'openingDate')),
                ('contractBeginDate', models.DateField(default=None, null=True, verbose_name='\u5408\u540c\u5f00\u59cb\u65f6\u95f4', db_column=b'contractBeginDate')),
                ('contractEndDate', models.DateField(default=None, null=True, verbose_name='\u5408\u540c\u7ed3\u675f\u65f6\u95f4', db_column=b'contractEndDate')),
                ('shop_brand', models.CharField(default=None, max_length=20, null=True, verbose_name='\u54c1\u724c', db_column=b'shopbrand')),
                ('areaId', models.ForeignKey(db_column=b'areaId', verbose_name='\u533a\u57dfID', to='cy.Area')),
                ('managerId', models.ForeignKey(db_column=b'managerId', verbose_name='\u9500\u552e\u7ecf\u7406', to='cy.Managers')),
            ],
            options={
                'db_table': 'shop-info',
                'verbose_name': '\u5e97\u94fa\u57fa\u7840\u4fe1\u606f',
                'verbose_name_plural': '\u5e97\u94fa\u57fa\u7840\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='datadiff',
            name='id_shop',
            field=models.ForeignKey(db_column=b'id_shop', verbose_name='\u5e97\u94faID', to='cy.ShopInfo'),
        ),
        migrations.AddField(
            model_name='area',
            name='manager',
            field=models.ForeignKey(db_column=b'manager', verbose_name='\u533a\u57df\u8d1f\u8d23\u4ebaID', to='cy.Managers'),
        ),
    ]
