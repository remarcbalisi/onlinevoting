from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^onlinevoting/$', views.user_login, name='user_login'),
    url(r'^onlinevoting/register/$', views.user_add, name='user_add'),
    url(r'^onlinevoting/home/$', views.user_home, name='user_home'),
    url(r'^onlinevoting/logout/$', views.user_logout, name='user_logout'),
    url(r'^onlinevoting/addposition/$', views.position_add, name='position_add'),
    url(r'^onlinevoting/addelection/$', views.election_add, name='election_add'),
    url(r'^onlinevoting/addparty/$', views.party_add, name='party_add'),
    url(r'^onlinevoting/addcollege/$', views.college_add, name='college_add'),
    url(r'^onlinevoting/viewposition/$', views.position_view, name='position_view'),
    url(r'^onlinevoting/vote/$', views.vote, name='vote'),
    url(r'^onlinevoting/addcandidate/$', views.candidate_add, name='candidate_add'),
    url(r'^onlinevoting/viewcandidate/$', views.candidate_view, name='candidate_view'),
    url(r'^onlinevoting/party/(?P<pk>[0-9]+)$', views.party, name='party'),
]