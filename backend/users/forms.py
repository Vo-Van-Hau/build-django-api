from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from .models import Profile
  
class CustomUserCreationForm(UserCreationForm):  
    
    # username = forms.CharField(label = 'username', min_length = 5, max_length = 150)  
    email = forms.EmailField(label = 'email')  
    # password1 = forms.CharField(label = 'password', widget = forms.PasswordInput)  
    # password2 = forms.CharField(label= 'Confirm password', widget = forms.PasswordInput)  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
  
    # # will prevent to enter duplicate username.
    # def username_clean(self):  
    #     username = self.cleaned_data['username'].lower()  
    #     new = User.objects.filter(username = username)  
    #     if new.count():  
    #         raise ValidationError('User Already Exist')  
    #     return username  
  
    # # will prevent to enter duplicate email.
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = User.objects.filter(email = email)  
    #     if new.count():  
    #         raise ValidationError('Email Already Exist')  
    #     return email  
  
    # # will check both passwords are matched or not
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError('Password don\'t match')  
    #     return password2  
  
    # save the data.
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']