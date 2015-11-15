from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^onlinevoting/$', views.index, name='index'),
    url(r'^onlinevoting/register/$', views.user_add, name='user_add'),
]