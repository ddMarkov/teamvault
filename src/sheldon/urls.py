from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('sheldon.apps.secrets.api_urls'), name='api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('sheldon.apps.secrets.urls'), name='secrets'),
    url(r'', include('sheldon.apps.accounts.urls'), name='accounts'),
)
