#coding=utf8
from django.db import models

# Create your models here.

class sequence(models.Model):
    ID=models.AutoField(primary_key=True,verbose_name=u'序号',auto_created=True)
    sequence_name=models.CharField(max_length=100,verbose_name=u'系列')

    class Meta:
        verbose_name=u'系列'
        verbose_name_plural=verbose_name
        db_table='product_sequence'
    def __unicode__(self):
        return self.sequence_name

class standard(models.Model):
    ID=models.AutoField(auto_created=True,primary_key=True,verbose_name=u'序号')
    standard_name = models.CharField(max_length=100, verbose_name=u'执行标准名')
    standard_no=models.CharField(max_length=255,verbose_name=u'执行标准号')

    class Meta:
        verbose_name=u'执行标准'
        verbose_name_plural=verbose_name
        db_table=u'product_standard'

    def __unicode__(self):
        return self.standard_name


class material(models.Model):
    ID=models.AutoField(primary_key=True,auto_created=True,verbose_name=u'序号')
    material_name=models.CharField(max_length=120,verbose_name=u'材料')

    class Meta:
        verbose_name=u'材料'
        verbose_name_plural=verbose_name
        db_table=u'product_material'
    def __unicode__(self):
        return self.material_name


class product_image(models.Model):
    ID=models.AutoField(primary_key=True,auto_created=True,verbose_name=u'序号')
    image_name=models.CharField(max_length=120,verbose_name=u'图片名称')
    image_path=models.ImageField(upload_to='productimage/')

    class Meta:
        verbose_name=u'产品图片'
        verbose_name_plural=verbose_name
        db_table=u'product_image'

    def __unicode__(self):
        return self.image_name



class product(models.Model):
    ID=models.AutoField(auto_created=True,primary_key=True,verbose_name=u'序号')
    product_sequence_id=models.ForeignKey(sequence,verbose_name=u'产品系列')
    product_no=models.CharField(max_length=40,verbose_name=u'产品编码',null=False)
    product_name=models.CharField(max_length=60,verbose_name=u'产品名称')
    product_sale_name=models.CharField(max_length=60,verbose_name=u'产品销售名称',null=True)
    product_image_id=models.ManyToManyField(product_image,verbose_name=u'产品图片',null=True)
    product_standard_id=models.ForeignKey(standard,verbose_name=u'产品执行标准')
    product_material_id=models.ManyToManyField(material,verbose_name=u'产品材料')
    product_instroduce=models.TextField(verbose_name=u'产品简介')

    class Meta:
        verbose_name=u'产品'
        verbose_name_plural=verbose_name
        db_table=u'product'

    def __unicode__(self):
        return self.product_name
