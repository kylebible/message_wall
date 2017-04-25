from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^loginpage$', views.login_page),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^wall$', views.wall),
    url(r'^logout$', views.logout),
    url(r'^add_message$', views.add_message),
    url(r'^user$', views.user_page),
    url(r'^like_message/(?P<id>\d+)$', views.add_like)
    url(r'^user/(?P<id>\d+)$', views.user_page),
    url(r'^logout$', views.logout)
]
