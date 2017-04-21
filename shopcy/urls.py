from django.conf.urls import include, url
from django.contrib import admin
from cy.views import *
from shopcy import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'shopcy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',shop,name='shop'),
    url(r'^addshop/', addshop, name='addshop'),
    url(r'^update_diff/', update_diff, name='update_diff'),
    url(r'^upsysamout/',excelindb,name='upsysamout'),
    url(r"^upload/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    # url(r'^delsys/(?P<del_id>[0-9]+)/', delete_sys_data, name='delsys'),
    url(r'^check/', addcheckdata, name='check'),
    url(r'^diff/', checkdata, name='diff')
]
