from django.conf.urls.defaults import patterns, include, url
from cal import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eastvantage.views.home', name='home'),
    # url(r'^eastvantage/', include('eastvantage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'cal.views.login_view', name='login_view'),
    url(r'^logout/', 'cal.views.logout_view', name='logout_view'),
    url(r'^$', 'cal.views.home_view', name='home_view'),
)
