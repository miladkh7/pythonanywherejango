from django.urls import path
from django.urls import include
from django.conf.urls import url
from . import views
from . import otherfunction
urlpatterns = [
    url(r'^signup/',views.sign_up,name='sing_up'),
    url(r'^RequestCode/',views.request_code,name='requset_code'),
    url(r'^ConfirmCode/',views.confrim_code,name='confirm_code'),
    url(r'^CreateMatchPage/CreateMatchReqeust/',views.create_match,name='create_match_request'),
    url(r'^CreateMatchPage/',views.create_match_page,name='create_match_page'),
    url(r'^CreateEventPage/',views.create_event_page,name='create_event_page'),
    url(r'^SendRequstMatch/',views.send_match_request,name='send_request_match'),
    url(r'^discoverMatchs/',views.discover_matchs,name='discover_matchs'),
    url(r'^RemoveSentRequest/',views.remove_match_sent_request,name='remove_sent_match_request'),
    url(r'^ManageRecivedRequest/',views.manage_match_join_request,name='manage_recived_match_request'),
    # url(r'^RemoveSentRequest/',views.reject_match_join_request,name='reject_match_join_request'),
    url(r'^JoinMatch/',views.joinMatch,name='match_join'),
    url(r'^together/',views.together,name='together'),
    url(r'^homepage/',views.home_page,name='homepage'),
    url(r'^edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/<profileId>/',views.view_profile),
    
    url(r'^userlogin/',views.login,name='userlogin'),

    url(r'^sendMessage/',views.send_moboile_massage,name='sendmsg')

]
