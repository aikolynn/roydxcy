"Commonly-used date structures"
#coding=utf8
from django.utils.translation import pgettext_lazy, ugettext_lazy as _

WEEKDAYS_zh = {
    0: _(u'星期一'),
    1: _(u'星期二'),
    2: _(u'星期三'),
    3: _(u'星期四'),
    4: _(u'星期五'),
    5: _(u'星期六'),
    6: _(u'星期日')
}
WEEKDAYS_ABBR_zh = {
    0: _(u'周一'),
    1: _(u'周二'),
    2: _(u'周三'),
    3: _(u'周四'),
    4: _(u'周五'),
    5: _(u'周六'),
    6: _(u'周日')
}


#农历月份别称
MONTHS_SPRING_ZH = {
    1: _(u'正月'),
    2: _(u'梅月'),
    3: _(u'花月'),
    4: _(u'农月'),
    5: _(u'仲夏'),
    6: _(u'暑月'),
    7: _(u'兰月'),
    8: _(u'正秋'),
    9: _(u'菊月'),
    10: _(u'吉月'),
    11: _(u'寒月'),
    12: _(u'腊月')
}
MONTHS_3_zh = {
    1: _(u'一月'),
    2: _(u'二月'),
    3: _(u'三月'),
    4: _(u'四月'),
    5: _(u'五月'),
    6: _(u'六月'),
    7: _(u'七月'),
    8: _(u'八月'),
    9: _(u'九月'),
    10: _(u'十月'),
    11: _(u'十一月'),
    12: _(u'十二月')
}
MONTHS_3_REV_zh = {
    u'壹月': 1,
    u'贰月': 2,
    u'叁月': 3,
    u'肆月': 4,
    u'伍月': 5,
    u'陆月': 6,
    u'柒月': 7,
    u'捌月': 8,
    u'玖月': 9,
    u'拾月': 10,
    u'拾壹月': 11,
    u'拾贰月': 12
}
MONTHS_AP_zh = {  # month names in Associated Press style
    1: pgettext_lazy('abbrev. month', 'Jan.'),
    2: pgettext_lazy('abbrev. month', 'Feb.'),
    3: pgettext_lazy('abbrev. month', 'March'),
    4: pgettext_lazy('abbrev. month', 'April'),
    5: pgettext_lazy('abbrev. month', 'May'),
    6: pgettext_lazy('abbrev. month', 'June'),
    7: pgettext_lazy('abbrev. month', 'July'),
    8: pgettext_lazy('abbrev. month', 'Aug.'),
    9: pgettext_lazy('abbrev. month', 'Sept.'),
    10: pgettext_lazy('abbrev. month', 'Oct.'),
    11: pgettext_lazy('abbrev. month', 'Nov.'),
    12: pgettext_lazy('abbrev. month', 'Dec.')
}
MONTHS_ALT_zh = {  # required for long date representation by some locales
    1: pgettext_lazy('alt. month', 'January'),
    2: pgettext_lazy('alt. month', 'February'),
    3: pgettext_lazy('alt. month', 'March'),
    4: pgettext_lazy('alt. month', 'April'),
    5: pgettext_lazy('alt. month', 'May'),
    6: pgettext_lazy('alt. month', 'June'),
    7: pgettext_lazy('alt. month', 'July'),
    8: pgettext_lazy('alt. month', 'August'),
    9: pgettext_lazy('alt. month', 'September'),
    10: pgettext_lazy('alt. month', 'October'),
    11: pgettext_lazy('alt. month', 'November'),
    12: pgettext_lazy('alt. month', 'December')
}
