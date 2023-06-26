from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
# Form: html에 있는 form 태그
# Model Form: model을 사용하는 form
# 유효성 검사를 위해서 이렇게 사용함
class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['email', 'name', 'password']


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']