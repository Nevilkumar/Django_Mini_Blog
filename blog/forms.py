from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext, gettext_lazy as _
from blog.models import Post

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class':'form-control my-2'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs = {'class':'form-control my-2'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control my-2'}),
        'email':forms.EmailInput(attrs = {'class':'form-control my-2'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs = {'autofocus':True,'class':'form-control my-2'}))

    password = forms.CharField(label='Password',strip=False, widget=forms.PasswordInput(attrs = {'autocomplete': 'current-password','class':'form-control my-2'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control my-2'}),
            'desc':forms.Textarea(attrs={'class':'form-control my-2'}),
        }