from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control','style': 'max-width: 300px;', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control','style': 'max-width: 300px;', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    class Meta:
        model = User
        fields = ["username", 'password1',"password2","first_name","last_name","email"] 
        widgets = {"username":forms.TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Name'}),
                   "first_name":forms.TextInput(attrs={"class":"form-control",'style': 'max-width: 300px;','placeholder': 'First Name'}),
                   "last_name":forms.TextInput(attrs={"class":"form-control",'style': 'max-width: 300px;','placeholder': 'LastName'}),
                   "email":forms.TextInput(attrs={"class":"form-control",'style': 'max-width: 300px;','placeholder': 'Email'}),
                   }
        
class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Name'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Password'}),
    )

    class Meta:
        fields = ["username", 'password'] 
        