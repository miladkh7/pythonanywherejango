from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from .otherfunction import default_start_time
# Create your models here.
class Token(models.Model):
    # user_id=models.CharField(max_length=16,blank=False)
    verify_state=models.BooleanField(default=False)
    token=models.CharField(max_length=48,null=False)
    password_hash=models.CharField(max_length=64)

    def __str__(self):
        return "{}-{}".format(self.user_id,self.verify_state)

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    # user_id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20,default='no name')
    last_name=models.CharField(max_length=20,default='no name')
    gender=models.CharField(max_length=5,null=True)
    profile_pic=models.ImageField(null=True,upload_to='profile_pic',default='profile-defulat.png')
    
    def __str__(self):
        return "{}-{}-{}".format(self.user.username,self.first_name,self.last_name)

class Match(models.Model):
    match_owner=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)#,null=True,on_delete=models.CASCADE,)
    match_place=models.CharField(max_length=20, null=True)
    match_time=models.TimeField(default=default_start_time)
    match_date=models.DateField()
    match_datej=jmodels.jDateField(null=True)
    match_type=models.CharField(max_length=20)
    match_players_No=models.PositiveIntegerField(null=True)
    match_length=models.PositiveIntegerField(null=True,default=90)
    match_code=models.AutoField(primary_key=True)
    match_game=models.CharField(max_length=25,default='footbal',null=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.match_owner,self.match_code,self.match_date,self.match_place)


class MatchRequest(models.Model):
    matchcode=models.ForeignKey(Match,on_delete=models.CASCADE)
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='itemone')
    reciver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='itemtwo')
    state=models.CharField(max_length=20)

    def __str__(self):
        return "{}-{}-{}".format(self.matchcode,self.sender,self.state)

class TempRegister(models.Model):
    user_name=models.CharField(max_length=20,primary_key=True)
    temp_pass=models.CharField(max_length=20)
    # gender=models.CharField(max_length=20)
    register_date_time=models.DateTimeField(null=True,blank=True)
    register_time_expire=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return "{}".format(self.user_name)
