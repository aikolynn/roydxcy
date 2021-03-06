# -*- coding: utf-8 -*-
from django.db import models



class Managers(models.Model):
    id = models.AutoField(unique=False, blank=False, null=False, verbose_name=u'用户ID', primary_key=True,auto_created=True)
    name = models.CharField(null=False, verbose_name=u'姓名', max_length=40)
    personal_cellphone = models.CharField(max_length=11, verbose_name=u'私人手机')
    company_cellphone = models.CharField(max_length=11, verbose_name=u'公司手机',null=True)
    qq = models.CharField(max_length=20, verbose_name=u'QQ', null=True, blank=True)
    email = models.EmailField(null=True, verbose_name=u'邮箱')
    title = models.CharField(verbose_name=u'职务', max_length=40, null=False)
    address = models.CharField(verbose_name=u'通讯地址', max_length=255)

    class Meta:
        verbose_name = u'区域管理人员信息表'
        verbose_name_plural = verbose_name
        db_table = 'Managers'

    def __unicode__(self):
        return self.name

class Area(models.Model):
    id=models.AutoField(unique=False,primary_key=True,verbose_name=u'区域ID',db_column='id',auto_created=True)
    name=models.CharField(max_length=40,verbose_name=u'区域名称',db_column='name',null=False)
    manager=models.ForeignKey(Managers,verbose_name=u'区域负责人ID',db_column='manager')
    class Meta:
        verbose_name=u'区域信息'
        verbose_name_plural=verbose_name
        db_table='area'
    def __unicode__(self):
        return  self.name

shopState=(
    ('S', u'正常营业'),
    ('Z',u'装修'),
    ('C', u'撤店'),
   ('P',u'暂停整改'),
)

shoptype=(
    ('D', u'直营'),
    ('A',u'代理'),
    ('J', u'加盟'),
   ('C',u'承包'),
)
class ShopInfo(models.Model):
    Id=models.AutoField(unique=False,auto_created=True,verbose_name=u'店铺ID',primary_key=True,db_column='Id')
    sName = models.CharField(max_length=255, blank=True, null=True,verbose_name=u'店铺名称',db_column='sName')
    sysName = models.CharField(max_length=255, blank=True, null=True,verbose_name=u'系统名称',db_column='sysName')
    areaId = models.ForeignKey(Area,verbose_name=u'区域ID',db_column='areaId')
    managerId=models.ForeignKey(Managers,verbose_name=u'销售经理',db_column='managerId')
    #店铺状态取值shopState
    state=models.CharField(max_length=2,verbose_name=u'运营状态',choices=shopState,db_column='state')
    mallType=models.CharField(max_length=3,verbose_name=u'卖场类型',db_column='mallTyep',null=True)
    shopType=models.CharField(max_length=2,verbose_name=u'经营方式',choices=shoptype,db_column='shopType')
    shopAddress=models.CharField(max_length=255,verbose_name=u'店铺地址',db_column='shopAddress')
    openingDate=models.DateField(default=None,verbose_name=u'开业时间',db_column='openingDate',auto_created=False,auto_now=False,auto_now_add=False)
    contractBeginDate=models.DateField(verbose_name=u'合同开始时间',db_column='contractBeginDate',null=True,default=None)
    contractEndDate=models.DateField(verbose_name=u'合同结束时间',db_column='contractEndDate',null=True,default=None)
    shop_brand=models.CharField(null=True,verbose_name=u'品牌',db_column='shopbrand',default=None,max_length=20)
    class Meta:
        verbose_name=u'店铺基础信息'
        verbose_name_plural=verbose_name
        db_table = 'shop-info'
    def __unicode__(self):
        return  self.sName
class saleflow(models.Model):
    sid=models.AutoField(auto_created=True,unique=False,verbose_name=u'流水ID',primary_key=True)
    id_shop=models.ForeignKey(ShopInfo,db_column='id_shop',verbose_name=u'店铺ID')
    flowNo=models.CharField(max_length=27,db_column='flowNo',verbose_name=u'销售单号')
    flow_No=models.CharField(max_length=5,db_column='flow_No',verbose_name=u'流水号')
    saleDate=models.DateField(blank=False,verbose_name=u'销售日期',db_column='saledate')
    productNo=models.CharField(max_length=255,db_column='productno',verbose_name=u'商品编码')
    productUnit=models.CharField(max_length=10,db_column='productunit',verbose_name=u'单位')
    productName=models.CharField(max_length=255,db_column='productname',verbose_name=u'商品名称')
    unitPrice=models.FloatField(blank=False,db_column='unitprice',verbose_name=u'商品单价')
    saleNumber=models.FloatField(blank=False,db_column='saleNumber',verbose_name=u'销售数量')
    saleAmount=models.FloatField(blank=False,db_column='saleAmount',verbose_name=u'应销金额')
    discountAmount=models.FloatField(blank=False,db_column='discountAmount',verbose_name='实收金额')

    class Meta:
        verbose_name=u'销售流水'
        verbose_name_plural=verbose_name
        db_table='saleflow'
    def __unicode__(self):
        return self.id_shop.sysName

class datadiff(models.Model):
    id = models.AutoField( unique=False, auto_created=True, verbose_name=u'账目ID',primary_key=True)
    id_shop = models.ForeignKey(ShopInfo, db_column='id_shop',verbose_name=u'店铺ID')
    date = models.DateField(blank=True, null=True,verbose_name=u'日期')
    shop_amount = models.FloatField(blank=True, null=True, verbose_name=u'上报金额',default=0)
    sys_amount = models.FloatField(blank=True, null=True, verbose_name=u'系统金额',default=0)
    amount = models.FloatField(blank=True, null=True,verbose_name=u'差异金额',default=0)
    diff=models.TextField(blank=True,null=True,verbose_name=u'差异原因')
    remark=models.TextField(blank=True,null=True,verbose_name=u'备注',default=u'未核查')
    true_amount=models.FloatField(default=shop_amount,null=True,db_column='true_amount',verbose_name=u'正确值')

    class Meta:
        ordering=['-date']
        verbose_name=u'差异表'
        verbose_name_plural=verbose_name
        db_table = 'datadiff'
    #覆写save方法，保存数据时amount=sys_aount-shop_amount
    def save(self,*args,**kwargs):
        if not self.pk:
            self.amount=self.sys_amount-self.shop_amount
            self.true_amount=self.shop_amount
            if self.amount != 0:
                self.remark = u'未核查'
        else:
            self.amount = self.sys_amount - self.shop_amount
            self.true_amount = self.shop_amount
            if self.amount != 0:
               self.remark = u'未核查'
        return super(datadiff,self).save(*args,**kwargs)

