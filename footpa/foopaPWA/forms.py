from django import forms

class SignUpForm(forms.Form):
    user_name=forms.CharField(max_length=25)

class ConfirmTempPassWord(forms.Form):
   confirm_code=forms.CharField(max_length=15)
   phone_number=forms.CharField(max_length=15)

class ProfileForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    gender=forms.CharField(max_length=5)
    profile_pic=forms.ImageField(allow_empty_file=True)