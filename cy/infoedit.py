#coding=utf-8
from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from models import  *
from forms import *
from django.http import JsonResponse
import  os
import json

def easy_ui_test(req):
    return render(req,'diff.html',locals())

def read_staff_info(req):
    page = req.GET['page']
    rows = req.GET['rows']
    manager = Managers.objects.all()
    total = {}
    row = []
    for m in manager:
        row.append(
            {
                "name": m.name,
                "title": m.title,
                "address": m.address,
                "qq": m.qq,
                "personal_cellphone": m.personal_cellphone,
                "company_cellphone": m.company_cellphone,
                "email": m.email,
            }
        )
    total["rows"] = row
    total["total"] = manager.count()
    easy_list = json.dumps(total)
    return HttpResponse(easy_list)

def staff(req):
    return  render(req,'staff.html',locals())
def shop_info(req):
    return render(req,'shopinfo.html',locals())
def read_shop_info(req):
     shop_info_all=ShopInfo.objects.all()
     data_json={}
     row=[]
     for shopinfo in shop_info_all:
         if shopinfo.contractBeginDate  is None:
             contractBeginDate=shopinfo.contractBeginDate
         else:
             contractBeginDate=shopinfo.contractBeginDate.strftime("%Y-%m-%d")
         if shopinfo.contractBeginDate is None:
             contractEndDate = shopinfo.contractEndDate
         else:
             contractEndDate = shopinfo.contractEndDate.strftime("%Y-%m-%d")
         row.append(
             {
                 "sname":shopinfo.sName,
                 "sysname":shopinfo.sysName,
                 "manager":shopinfo.managerId.name,
                 "malltype":shopinfo.mallType,
                 "area":shopinfo.areaId.name,
                 "shopAddress":shopinfo.shopAddress,
                 "brand":shopinfo.shop_brand,
                 "state":shopinfo.get_state_display(),
                 "shoptype":shopinfo.get_shopType_display(),
                 "openingDate":shopinfo.openingDate.strftime("%Y-%m-%d"),
                 "contractBeginDate":contractBeginDate,
                 "contractEndDate":contractEndDate

             }
         )
     data_json["rows"]=row
     data_json["total"]=shop_info_all.count()
     data_json_response=json.dumps(data_json)
     return HttpResponse(data_json_response)