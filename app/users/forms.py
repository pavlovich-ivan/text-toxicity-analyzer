from django import forms
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "first_name", "last_name")

class UserUpdateForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        fields = ("username", "email", "first_name", "last_name")