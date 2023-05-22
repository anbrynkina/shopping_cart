from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        # 'class': "form-control py-4", - moving this to def __init__
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'class': "form-control py-4",
        'placeholder': 'Enter your password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # adding one class for all fields ('class': "form-control py-4")
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control py-4"


class UserRegistrationForm(UserCreationForm):
    firs_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # adding one class for all fields ('class': "form-control py-4")
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control py-4"