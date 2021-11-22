from .models import User, Profile, UserAgent
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class CustomerSignUpForm(UserCreationForm):
    customer = Profile

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        customer = Profile.objects.create(user=user)
        return user


class UserAgentSignUpForm(UserCreationForm):
    #availability = forms.BooleanField()
    #agent = Agent
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 3
        user.save()
        useragent = UserAgent.objects.get_or_create(user=user)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'name':'name', 'placeholder':'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'name', 'name':'name', 'placeholder':'Password'}))

class ContactMessageForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'name':'name', 'placeholder':'Name..'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name':'email', 'placeholder':'Email..' }))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'subject', 'name':'phone', 'placeholder':'Subject..'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'6', 'id':'message', 'name':'message', 'placeholder':'Your Message Here...'})) 

