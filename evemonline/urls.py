from django.conf.urls import patterns, include, url
from rest_framework import routers
from api import views
from django.contrib import admin
admin.autodiscover()

# router = routers.DefaultRouter()
# router.register('apitoken', views.ApiToken)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evemonline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^apitoken/(?P<user_id>[0-9]+)$', 'api.views.api_token_list'),
    url(r'^admin/', include(admin.site.urls)),
)
