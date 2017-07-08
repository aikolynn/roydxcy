from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from models import  *
from forms import *
from django.http import JsonResponse
from django.db.models import Sum

def area_arr(req):
    area_a=datadiff.objects.raw('''
            SELECT
                    areaname,
                    sum(amou) shopamount
                    
            FROM
                (
                    SELECT
                        datadiff.sys_amount AS amou,
                        `shop-info`.sName AS n,
                        area.`name` AS areaname,
                        Managers.`name` as man,
                        MONTH(datadiff.date) as m
                 
                    FROM
                        datadiff
                    
                    LEFT JOIN `shop-info` ON datadiff.id_shop = `shop-info`.Id
                    LEFT JOIN area ON `shop-info`.areaId = area.Id
                    LEFT JOIN Managers on `shop-info`.managerId=Managers.id
                   WHERE MONTH (datadiff.date)=5
                ) AS basicquery
            GROUP BY areaname
    ''').query
    data=[]
    categories=[]
    # categories=tuple(area_a.cursor[0])
    for i in tuple(area_a):
        data.append(i[0])
        categories.append(i[1])

    return  render(req,'highcharts/highchart.html',locals())