from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^onlinevoting/$', views.index, name='index'),
    url(r'^onlinevoting/register/$', views.user_add, name='user_add'),
    url(r'^onlinevoting/login/$', views.user_login, name='user_login'),
    url(r'^onlinevoting/logout/$', views.user_logout, name='user_logout'),
    url(r'^onlinevoting/home/$', views.user_home, name='user_home'),
]