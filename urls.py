from django.conf.urls.defaults import *
from django.conf import settings
import api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^dojango/', include('dojango.urls')),
    (r'^api/', include('api.urls')),
    (r'^$', 'core.views.show'),
    (r'^show/(?P<id>.+)/$', 'core.views.show_form'),
    (r'^mptree/$', 'core.views.show_tree'),
    (r'^dojotree/$', 'core.views.dojo_tree'),
    (r'^tabcontainer/$', 'core.views.show_tab_container'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
