from django.conf.urls.defaults import *
from django.conf import settings 
from django.contrib.auth.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^learn/', include('learnOnline.learn.urls')),
    # Example:
    # (r'^learnOnline/', include('learnOnline.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns += patterns('django.views.static',
		(r'^%s(?P<path>.*)$' % (settings.MEDIA_URL[1:],), 'serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True }),)
