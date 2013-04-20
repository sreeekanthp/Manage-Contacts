from django.conf.urls import patterns, include, url
from django.contrib import admin
from contacts import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^admin/', include(admin.site.urls), name='admin'),
	url(r'^contacts/', include('contacts.urls')),
	url(r'^contracts/', include('contracts.urls')),
	url(r'^groups/', include('groups.urls')),
	url(r'^members/', include('members.urls')),

)
