from django.conf.urls import patterns, include, url
from store import urls as app_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(app_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
