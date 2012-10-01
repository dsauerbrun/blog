from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
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
	(r'^home$','posting.views.index'),
	(r'^addPayment$','moneytracker.views.addPayment'),
	(r'^expenseReport$','moneytracker.views.expenseReport'),
	(r'&add_expense/(\d+)/$','moneytracker.views.add_expense'),
	(r'&add_comment/(\d+)/$','posting.views.add_comment'),
	(r'&delete_comment/(\d+)/$','posting.views.delete_comment'),
	(r'^addlocation','posting.views.add_location'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','posting.views.index',name='blog_index'),
    url(r'^login/$','auth.views.login_user'),
    url(r'^media_files/uploads/(?P<path>.*)$', 'django.views.static.serve',
        #{'document_root': 'media_files/'}),
        {'document_root': settings.MEDIA_ROOT+'/uploads/'}),
#        {'document_root': '/srv/www/blog/media_files/uploads/'}),
)
urlpatterns += staticfiles_urlpatterns()
