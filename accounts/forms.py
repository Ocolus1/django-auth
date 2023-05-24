from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
from .models import CustomUser
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("name", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("name", "email")
        
        
class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=30, label='Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.save()
        return user
