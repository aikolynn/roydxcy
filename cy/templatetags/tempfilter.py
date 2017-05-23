#coding=utf-8
from django.utils.dateformat import *
from django import template
from dates_zh import *
from django.conf import *
from django.utils import formats



register=template.Library()

@register.filter(expects_localtime=True, is_safe=False)
def zh_date(value, arg=None):
    """Formats a date according to the given format."""
    if value in (None, ''):
        return ''
    if arg is None:
        arg = settings.DATE_FORMAT
    try:
        return formats.date_format(value, arg)
    except AttributeError:
        try:
            return format(value, arg)
        except AttributeError:
            return ''


settings = LazySettings()