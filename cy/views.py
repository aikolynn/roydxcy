#coding=utf-8

from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from models import  *
from forms import *
from django.http import JsonResponse
# Create your views here.
#展示店铺信息并增加修改店铺信息
def shop(request):
     shop_list=ShopInfo.objects.all()
     man_list=Managers.objects.all()
     area_list=Area.objects.all()
     return render(request,'shop.html',locals())
#添加店铺信息


def addinfo(req):
    sava_message = {"sava_message": "保存成功"}
    action=req.GET['action']
   #判断添加信息类型：manager--添加人员信息 area--添加区域信息 shopinfo--添加店铺信息
   #添加人员信息
    if action=='manager':
        Managers.objects.create(
            name=req.GET['manager_name'],
            personal_cellphone=req.GET['manager_phone'],
            company_cellphone=req.GET['manager_c_phone'],
            qq=req.GET['manager_qq'],
            title=req.GET['manager_title'],
            email=req.GET['manger_email'],
            address=req.GET['manager_address']
        )
     #添加区域信息
    elif action=='area':
        manager_name=Managers.objects.get(id=req.GET['area_manager'])
        print manager_name
        Area.objects.create(
            manager=manager_name,
            name=req.GET["area_name"]
        )
     #添加店铺信息
    elif action=="shopinfo" :
        sys_name = req.GET['sys_name']
        s_name = req.GET['s_name']
        sale_manager = Managers.objects.get(id=req.GET['sale_manager'])
        aree = Area.objects.get(id=req.GET['area'])
        shoptype = req.GET['shoptype']
        malltype = req.GET['malltype']
        opendate = req.GET['openingdate']
        shopadd = req.GET['shopadd']
        conbengin = req.GET['contractBegindate']
        conEnd = req.GET['contractEndDate']
        shopstate = req.GET['shopstate']
        ShopInfo.objects.create(sysName=sys_name,
                                sName=s_name,
                                managerId=sale_manager,
                                areaId=aree,
                                shopType=shoptype,
                                mallType=malltype,
                                openingDate=opendate,
                                shopAddress=shopadd,
                                contractBeginDate=conbengin,
                                contractEndDate=conEnd,
                                state=shopstate)
    return JsonResponse(sava_message)
def update_amount(update):
    pass
def addcheckdata(req):
    sava_message = {"sava_message": "提交成功"}
    shopname=ShopInfo.objects.get(Id=req.GET["shop_name"])
    data_date=req.GET["data_date"]
    shop_amount_report = float(req.GET["money"])
    #根据data_date和shopname查询是否存在记录，如存在则更新，否则新建
    if datadiff.objects.filter(date=data_date,id_shop=shopname).count():
        #获取原有记录中的sys_amount
        sys_amount_exists=datadiff.objects.get(date=data_date, id_shop=shopname).sys_amount
        #更新记录中的shop_amount和amount
        datadiff.objects.filter(date=data_date, id_shop=shopname).update(shop_amount=shop_amount_report,amount=sys_amount_exists-shop_amount_report)
    else:

        create_list = datadiff(date=data_date, shop_amount=shop_amount_report, id_shop=shopname)
        create_list.save()
    return JsonResponse(sava_message)

#获取所有有差异的数据
def checkdata(request):
    shop_list = ShopInfo.objects.all()
    diff=datadiff.objects.exclude(amount=0).order_by("id_shop","-date")
    return render(request,'checkdata.html',locals())
#修改差异原因
def update_diff(req):
    sava_message = {"sava_message": "提交成功"}
    diff_new=req.GET["diff_new"]
    diff_id=req.GET["diff_id"]
    datadiff.objects.filter(id=diff_id).update(diff=diff_new)
    return  JsonResponse(sava_message)

import os
import  openpyxl
import xlrd
def excelindb(request):
    sava_message = "上传成功"
    excel_file = request.FILES['excelfile']
    excel_date = request.POST["exceldate"]
    with open('static/upload/' + excel_date + '.xlsx', 'wb+') as destination:
        for chunk in excel_file.chunks():
            destination.write(chunk)
    destination.close()
    excel_data = openpyxl.load_workbook("static/upload/"+excel_date+".xlsx")
    sheetnames = excel_data.get_sheet_names()
    excel_sheets=excel_data.get_sheet_by_name(sheetnames[0])
    excel_rows=excel_sheets.max_row
    excel_columns=excel_sheets.max_column
    print excel_rows,excel_columns
    #循环读取每行数据然后写入数据库
    for i in range(2,excel_rows+1):
        j=1
        #excel表格从第二行开始读取，每行第一列为店铺名
        shop_id=ShopInfo.objects.get(sName=(excel_sheets.cell(row=i,column=j).value))
        #每行第二列为系统金额
        sys_amount_excel=float(excel_sheets.cell(row=i,column=j+1).value)
        #根据时间（excel_date）和店铺名称（shop_id）来判断记录是否存在，如果存在更新原有记录，否则新建记录
        if datadiff.objects.filter(date=excel_date, id_shop=shop_id).count():
            shop_amount_excel = datadiff.objects.get(date=excel_date, id_shop=shop_id).shop_amount
            datadiff.objects.filter(date=excel_date, id_shop=shop_id).update(sys_amount=sys_amount_excel, amount=sys_amount_excel-shop_amount_excel)
        else:
            sys_diff=datadiff(sys_amount=sys_amount_excel,date=excel_date,id_shop=shop_id)
            sys_diff.save()
    return render(request,'checkdata.html',sava_message)
