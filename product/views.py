#coding=utf8
from django.shortcuts import render
from  models import *
# Create your views here.
#产品列表
def product_view(request):
    product_list=product.objects.all()
    image_list=product.product_image_id.all()
    return  render(request,'product/viewproduct.html',locals())

