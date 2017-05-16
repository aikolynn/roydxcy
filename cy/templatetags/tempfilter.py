#coding=utf-8
from django.utils.dateformat import *
from django import template

register=template.Library()

class zh_data_format(DateFormat):
    #时间格式化为“*周”
    def CW(self):
       week=(self.data.weekday() + 1) % 7
       return "%s+周" %week

    def CM(self):
        
        return MONTHS[self.data.month]
