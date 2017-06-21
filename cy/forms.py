#coding=utf-8
from models import *
from django import  forms


#
class checkdataform(forms.ModelForm):
    class Meta:
        model=Area
        fields={'name','manager'}
        labels={
            'name':'区域名称',
            'manager':'负  责  人',
        }
        widgets={
            'name':forms.TextInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': '请输入昵称',

                }),
            'manager':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '请输入昵称',
            }),

        }
