from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^$', views.post_list, name='post_list'),
]
