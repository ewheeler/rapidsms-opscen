import os
from django.conf.urls.defaults import *
from django.contrib import admin
import settings

handler500 = 'djangotoolbox.errorviews.server_error'
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^admin/', include(admin.site.urls)),

    # RapidSMS core URLs
    url(r'^$', 'views.dashboard', name='rapidsms-dashboard'),
)
