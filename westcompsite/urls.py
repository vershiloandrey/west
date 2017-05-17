from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^pcs/$', views.pcs, name='pcs'),
    url(r'^complect/$', views.complect, name='complect'),
    url(r'^periphery/$', views.periphery, name='peryphery'),
    url(r'^access/$', views.access, name='access'),
    url(r'^remont/$', views.remont, name='remont'),
]
