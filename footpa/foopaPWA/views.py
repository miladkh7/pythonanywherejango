from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import Match,Profile,User,MatchRequest,TempRegister
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from .otherfunction import mobile_massage
from unidecode import unidecode
from datetime import datetime,timedelta
import jdatetime
import random
import math
from .otherfunction import jalali_str_to_gorgian_date,send_my_msg
from django.utils import timezone
from .forms import SignUpForm,ConfirmTempPassWord,ProfileForm
from django.contrib.auth.models import User
# Create your views here.

def send_moboile_massage(request):
    print('this')
    reciver="09352997106"
    content="hi this is activation method"
    mobile_massage(reciver,content)
    return (HttpResponse('massage sent'))

def sign_up(request):
    singup_form=SignUpForm()
    ctx={'form':singup_form}
    return render(request,'singup.html',ctx)

def request_code(request):
    singup_form=SignUpForm(request.POST)
    temp_use_name=request.POST['user_name']
    start_time=timezone.now()   
    end_time=start_time+timedelta(minutes=4)
    #Todo:make sure active code are exactly 6 digit
    otp_temp_pass=math.floor(random.random() * 1e6)
    # otp_temp_pass=123456 #for test
    mobile_message_content="your activation code is {}".format(otp_temp_pass)

    obj, created = TempRegister.objects.update_or_create(
    user_name=temp_use_name, defaults={'register_date_time':start_time,
    'register_time_expire':end_time,'temp_pass':otp_temp_pass})
    #it test we dont need any temp pass
    mobile_massage(temp_use_name,mobile_message_content)

    confirmPass_instance=ConfirmTempPassWord({'phone_number': temp_use_name})
    ctx={'form':confirmPass_instance}
    return render(request,'confirmTempCode.html',ctx)

def confrim_code(request):
    print('salam')
    confirmPass_instance=ConfirmTempPassWord(request.POST)
    print(request.POST)
    temp_user_name=request.POST['phone_number']
    user_enterd_code=request.POST['confirm_code']
    related_user=TempRegister.objects.filter(user_name=temp_user_name).get()
    correctPassword=related_user.temp_pass
    expire_time=related_user.register_time_expire
    submit_time=timezone.now()
    print(expire_time)
    print(submit_time)
    ctx={'state':'nothing'}
    if expire_time>= submit_time:
        # print('password is not expire')
        
        if user_enterd_code==correctPassword:
            print('createNewUser')
            newuser = User.objects.create_user(temp_user_name, 'test@gmail.com', temp_user_name)
            # newuser.save()
            print(newuser)
            Profile.objects.create(user=newuser)
            authenticated_user=authenticate(username=newuser,password=newuser)
            login(request,authenticated_user)
            return redirect('/profile/temp_user_name/')
        else:
            return HttpResponse('its not correct code ')
    else:
        ctx={'state':'expired pass'}
        return HttpResponse('password is expired')
    

def create_match_page(requset):
    return render(requset,'newMatchPage.html')

def create_event_page(request):
    return HttpResponse('create event')

@login_required
def create_match(request):
    print('in creating match')
    username = None
    ctx={}
    if request.user.is_authenticated:

        username = request.user.username
        # print('we ar loged in by accont ' + username)
        # print(request.POST)
        this_match_place=request.POST['match-place']
        this_match_time=request.POST['match-time']
        this_match_datej=unidecode(request.POST['match-date'])
        this_match_type=request.POST['match-type']
        this_match_players_No=request.POST['match-player-no']
        this_match_length=request.POST['match-length'] 
        this_match_game='footbal'
        this_match_datej=this_match_datej.replace("/","-")
        this_match_date=jalali_str_to_gorgian_date(this_match_datej)
        Match.objects.create(match_owner=request.user,match_place=this_match_place,
        match_time=this_match_time,match_date=this_match_date,match_datej=this_match_datej,match_type=this_match_type,
        match_players_No=this_match_players_No,match_length=this_match_length,match_game=this_match_game)
        
    # return render(request,'discoverPage.html')
    return redirect('/discoverMatchs/')

def send_match_request(request):
    return HttpResponse('match request sent')
@login_required
def discover_matchs(request):
    # matchs=Match.objects.all()
    if request.user.is_authenticated:
        username = request.user
    matchs=Match.objects.exclude(match_owner=username)
    # match_list={'open_match':matchs}
    ctx={'match_list':matchs}
    return render(request,'discoverPage.html',ctx)
    # return render(request,'discoverPage.html',match_list)

def login_user(request):
    HttpResponse('we are login')
@login_required
def view_profile(request,profileId):
    print('this is my profile')
    profile_page=ProfileForm()
    
    ctx={'form':profile_page}
    return render(request,'userProfile.html',ctx)

@login_required
def edit_profile(request):
    username = None
    ctx={}
    if request.user.is_authenticated:
        username = request.user
    profile_page=ProfileForm()
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    gender=request.POST['gender']
    profile_pic=request.POST['profile_pic']
    obj, created = Profile.objects.update_or_create(
    user=username, defaults={'first_name':first_name,
    'last_name':last_name,'gender':gender,'profile_pic':profile_pic})
    # ctx={'form':profile_page}
    return redirect('/homepage/')

@login_required
def home_page(request):
    username = None
    ctx={}
    if request.user.is_authenticated:
        print("user loged in ")
        username = request.user.username
        print(username)

        profiles_info=Profile.objects.filter(user=request.user).get()
        # profiles_info=Profile.objects.get(user_request.user)
        # print(profiles_info.last_name)
        # person=profiles_info[0]
        full_name="{} {}".format(profiles_info.first_name,profiles_info.last_name)
        # print(full_name)
        ctx={'name':full_name,'image':profiles_info.profile_pic}
        print('now we want to see home page')
    return render(request,'homePage.html',ctx)

@login_required
def joinMatch(request):
    username = None
    ctx={}
    if request.user.is_authenticated:
        username = request.user.username
        current_match_code=request.POST['match-code']
        # print("match code : " +current_match_code)
        request_reciver=Match.objects.filter(match_code=current_match_code).get()
        request_reciver_user=request_reciver.match_owner
        # print(username)
        # print('salam')
        # print(request_reciver_user.username)
        same_match_no=MatchRequest.objects.filter(matchcode=request_reciver,sender=request.user,reciver=request_reciver_user).count()
        # print("the number of same match is {}".format(same_match_no))
        if not same_match_no>0:
            MatchRequest.objects.create(matchcode=request_reciver,sender=request.user,reciver=request_reciver_user,state='send request')
        return redirect('/discoverMatchs/')
    return HttpResponse("error ocured")

@login_required
def together(request):
    username = None
    ctx={}
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        # recive request from others
        user_recived_request_matchs=MatchRequest.objects.filter(reciver=request.user)


        #send requst to others
        user_sent_request_matchs=MatchRequest.objects.filter(sender=request.user)
        # for mymatch in user_sent_request_matchs:
            # print(mymatch.matchcode.match_code)

        #crate match request
        user_created_matchs=Match.objects.filter(match_owner=request.user)

        # ctx={'own_created_match':user_created_matchs,}
        ctx={'own_sent_request':user_sent_request_matchs,'own_recived_request':user_recived_request_matchs}
        return render(request,'togetherPage.html',ctx)
    return HttpResponse("error ocured")

@login_required
#Todo:its beter to use cancel request
def remove_match_sent_request(request):
    username = None
    ctx={}
    if request.user.is_authenticated:
        # print('we want to deltet request')
        request_to_delete_code=request.POST['match-request-code']
        # print(request_to_delete_code)
        MatchRequest.objects.filter(matchcode__match_code=request_to_delete_code).delete()
    return redirect('/together/')

@login_required
def manage_match_join_request(request):
    print("want to manage jorin request")
    username = None
    ctx={}
    if request.user.is_authenticated:
            # print('we want to deltet request')
        request_type=request.POST['match_request_action']
        request_to_manage_code=request.POST['match-request-code']
        if request_type=="accept":
            print('acceptd request')
        elif request_type=='reject':
            MatchRequest.objects.filter(matchcode__match_code=request_to_manage_code).delete()
    return redirect('/together/')