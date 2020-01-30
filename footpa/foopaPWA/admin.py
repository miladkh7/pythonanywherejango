from django.contrib import admin
from .models import Match,Token,Profile,MatchRequest,TempRegister
# Register your models here.
admin.site.register(Token)
admin.site.register(Profile)
admin.site.register(Match)
admin.site.register(MatchRequest)
admin.site.register(TempRegister)