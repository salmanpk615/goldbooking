from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from .models import Items


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email', 'phone')

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('name', 'email', 'phone')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = "__all__"


