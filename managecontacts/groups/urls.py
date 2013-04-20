from django.conf.urls import patterns, include, url
from django.contrib import admin
from groups import views

admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^group/$', views.group, name='group'),
	url(r'^email/(?P<group_id>\d+)/$', views.email, name='email'),


)
