from django.conf.urls import patterns, include, url
from django.contrib import admin
from contracts import views

admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^contract/$', views.contract, name='contract'),

)
