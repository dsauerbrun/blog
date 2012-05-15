from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
	(r'^login$','blog.auth.views.login_user'),
#	(r'^$','blog.views.index'),
	(r'^home$','blog.views.index'),
	(r'&add_comment/(\d+)/$','blog.views.add_comment'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index',name='blog_index'),
    url(r'^login/$','auth.views.login_user'),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media_files/uploads/'}),
)
urlpatterns += staticfiles_urlpatterns()
