from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qxt.views.home', name='home'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': r'e:\qxt\qxt\static'}),
     url(r'^iget/', include('qxt.iget.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
