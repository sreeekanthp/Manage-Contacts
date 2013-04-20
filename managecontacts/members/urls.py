from django.conf.urls import patterns, include, url
from django.contrib import admin

from members import views

admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^member/$', views.member, name='member'),
	url(r'^upload_file/$', views.upload_file, name='upload_file'),

)
