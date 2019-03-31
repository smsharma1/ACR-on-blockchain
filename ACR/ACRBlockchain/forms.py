from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','user_type')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','user_type')

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


    # comment = forms.CharField()
    # fields = ('name', 'url','comment')
