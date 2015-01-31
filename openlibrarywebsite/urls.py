from django.conf.urls import patterns, url
from openlibrarywebsite import views



urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)