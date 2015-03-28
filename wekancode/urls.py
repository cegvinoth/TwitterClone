from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wekancode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),url(r'^$','Interview.views.index'),url(r'^login$','Interview.views.login'),url(r'^home$','Interview.views.home'),url(r'^logout$','Interview.views.logout'),
)
