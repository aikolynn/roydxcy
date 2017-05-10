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
    url(r'^addinfo/', addinfo, name='addinfo'),
    url(r'^update_diff/', update_diff, name='update_diff'),
    url(r'^upinfo/',excelindb,name='upinfo'),
    url(r"^upload/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    url(r'^check/', addcheckdata, name='check'),
    url(r'^diff/', checkdata, name='diff')
]
