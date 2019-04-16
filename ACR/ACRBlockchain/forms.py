from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, LeaveRecord, Appraisal
from .models import Card, AuthToken
from django.contrib.admin.widgets import AdminDateWidget

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','firstname','lastname','user_type')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','firstname','lastname','user_type')

class Ratee_submit_appraisal_application(forms.Form):
    Name = forms.CharField(max_length=100)
    Number = forms.CharField(max_length=10)
    USER_TYPE_CHOICES =(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('E','E'),
    )
    Rank= forms.CharField(label='What is your Rank', widget=forms.Select(choices=USER_TYPE_CHOICES))


class LeaveRecord(forms.ModelForm):
    class Meta:
        model = LeaveRecord
        # widgets = {
        #     'To': forms.DateInput(attrs={'class':'datepicker'}),
        #     'From': forms.DateInput(attrs={'class':'datepicker'}),
        # }
        # widgets = {
        #     'To': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        # }
        widgets = {
            'To': AdminDateWidget(),
            'From': AdminDateWidget(),
        }
        fields = ('OfficerID','From','To')

class Appraisal(forms.ModelForm):
    class Meta:
        model = Appraisal
        fields = ('RateeID','IOID','ROID','SROID','AOID','ClerkID')

class MarkAttendance(forms.Form):
    OfficerID = forms.IntegerField()

class AuthToken(forms.ModelForm):
    class Meta:
        model = AuthToken    
        fields = ('OfficerID','AuthToken')


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('OfficerID','name','document',)