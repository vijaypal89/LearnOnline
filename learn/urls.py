from django.conf.urls.defaults import *
from learnOnline.learn import views
urlpatterns = patterns('',
	(r'^$', views.learning),
	(r'^school/$', views.baselearn),
	(r'^login/$', views.login),
	(r'^study/$', views.study),
	(r'^signup/$', views.signup),
)
