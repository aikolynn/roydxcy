#coding=utf8
from django.shortcuts import render
from  models import *
# Create your views here.
#产品列表
def product_view(request):
    image_list=product_image.objects.all()

    return  render(request,'product/viewproduct.html',locals())

