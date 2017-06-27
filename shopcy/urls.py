#coding= utf-8
from django.conf.urls import include, url
from django.contrib import admin
from cy.views import *
from cy.infoedit import *
from cy.highcharts import *
from product.views import *
from shopcy import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'shopcy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',shop,name='shop'),
    url(r'^addinfo/', addinfo, name='addinfo'),
    url(r'^update_diff/', update_diff, name='update_diff'),
    url(r'^upinfo/',excelindb,name='upinfo'),
    url(r"^upload/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    url(r'^check/', addcheckdata, name='check'),
    url(r'^diff/', checkdata, name='diff'),
    url(r'^checkall/',checkall,name='checkall'),
    url(r'^diff_excel_export',diff_export_excel,name="diff_export_excel"),
    url(r'^form/',fo,name='form'),
    url(r'^staff',staff,name='staff'),

    url(r'^productview/',product_view,name='productview'),

    url(r'^highchart/',area_arr,name="highchartarea"),

    #档案管理相关
    url(r'^easy/',read_staff_info,name='easy'),
    url(r'^test/',staff,name='test'),
    url(r'^firstui/',easy_ui_test,name='easyui'),
    url(r'^shopinfo/',shop_info,name='shopinfo'),
    url(r'^readshopinfo',read_shop_info,name='readshopinfo'),
]
