from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^onlinevoting/$', views.user_login, name='user_login'),
    url(r'^onlinevoting/register/$', views.user_add, name='user_add'),
    url(r'^onlinevoting/logout/$', views.user_logout, name='user_logout'),
    url(r'^onlinevoting/updateuser/$', views.user_update, name='user_update'),
    url(r'^onlinevoting/addposition/$', views.position_add, name='position_add'),
    url(r'^onlinevoting/deleteposition/(?P<position_pk>[0-9]+)/$', views.position_delete, name='position_delete'),
    url(r'^onlinevoting/viewposition/$', views.position_view, name='position_view'),
    url(r'^onlinevoting/addelection/$', views.election_add, name='election_add'),
    url(r'^onlinevoting/updateelection/$', views.election_update, name='election_update'),
    url(r'^onlinevoting/deleteelection/$', views.election_delete, name='election_delete'),
    url(r'^onlinevoting/viewelection/$', views.election_view, name='election_view'),
    url(r'^onlinevoting/addparty/$', views.party_add, name='party_add'),
    url(r'^onlinevoting/voterhome/$', views.voters_view, name='voters_view'),
    url(r'^onlinevoting/updateparty/(?P<party_pk>[0-9]+)/$', views.party_update, name='party_update'),
    url(r'^onlinevoting/addcandidate/$', views.candidate_add, name='candidate_add'),
    url(r'^onlinevoting/viewcandidate/$', views.candidate_view, name='candidate_view'),
    url(r'^onlinevoting/addcollege/$', views.college_add, name='college_add'),
    url(r'^onlinevoting/addbulletin/$', views.bulletin_add, name='bulletin_add'),
    url(r'^onlinevoting/vote/$', views.vote, name='vote'),
    url(r'^onlinevoting/viewparty/$', views.party_view, name='party_view'),
    url(r'^onlinevoting/party/(?P<pk>[0-9]+)/$', views.party, name='party'),
    url(r'^onlinevoting/position/(?P<pk>[0-9]+)/$', views.position, name='position'),
    url(r'^onlinevoting/viewcollege/$', views.college_view, name='college_view'),
    url(r'^onlinevoting/college/(?P<pk>[0-9]+)/$', views.college, name='college'),
    url(r'^onlinevoting/viewbulletin/$', views.bulletin_view, name='bulletin_view'),
    url(r'^onlinevoting/updatebulletin/$', views.bulletin_update, name='bulletin_update'),
    url(r'^onlinevoting/home/$', views.user_home, name='user_home'),
    url(r'^onlinevoting/view/(?P<pk>[0-9]+)', views.candidate, name='candidate'),
    url(r'^onlinevoting/userprofile/(?P<user_pk>[0-9]+)/$', views.user_profile, name='user_profile'),
    url(r'^onlinevoting/viewuser/$', views.user_view, name='user_view'),
    url(r'^onlinevoting/tally/$', views.count_tally, name='count_tally'),
    url(r'^onlinevoting/viewtally/$', views.view_tally, name='view_tally'),
    url(r'^onlinevoting/deletecandidate/(?P<candidate_pk>[0-9]+)/$', views.delete_candidate, name='delete_candidate'),
    url(r'^onlinevoting/deleteparty/(?P<party_pk>[0-9]+)/$', views.delete_party, name='delete_party'),
    url(r'^onlinevoting/updateposition/(?P<position_pk>[0-9]+)/$', views.position_update, name='position_update'),
    url(r'^onlinevoting/deletebulletin/(?P<bulletin_pk>[0-9]+)/$', views.delete_bulletin, name='delete_bulletin'),
    url(r'^onlinevoting/votervote/$', views.voters_vote, name='voters_vote'),
]