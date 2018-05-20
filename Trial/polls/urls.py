from django.conf.urls import patterns,url
from polls import views
urlpatterns = patterns('',
  url(r'^$',views.index,name='index' ),)

from django.conf.urls import url 
from . import views 
urlpatterns = [ url(r'^$', views.index, name='index'), ]
