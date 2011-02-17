import os
from django.conf.urls.defaults import *
from django.contrib import admin
import settings

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^admin/', include(admin.site.urls)),

    # RapidSMS core URLs
    url(r'^$', 'views.dashboard', name='rapidsms-dashboard'),

    # serve assets via django, during development
    url(r'^rapidsms/javascripts/(?P<path>.*)$', "django.views.static.serve",
    {"document_root": os.path.dirname(__file__) + "/static/javascripts"}),
    url(r'^rapidsms/stylesheets/(?P<path>.*)$', "django.views.static.serve",
    {"document_root": os.path.dirname(__file__) + "/static/stylesheets"}),
    url(r'^rapidsms/images/(?P<path>.*)$', "django.views.static.serve",
    {"document_root": os.path.dirname(__file__) + "/static/images"}),
    url(r'^rapidsms/icons/(?P<path>.*)$', "django.views.static.serve",
    {"document_root": os.path.dirname(__file__) + "/static/icons"}),
)
