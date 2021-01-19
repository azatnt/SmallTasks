from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from Requests.forms import *


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ("Пароль")})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ("Подтвердите")})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Никнейм'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }

        help_texts = {
            'username': None
        }


class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Никнейм'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'Пароль'})
        self.fields['password'].label = False


# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Requests
#         fields = ('file')