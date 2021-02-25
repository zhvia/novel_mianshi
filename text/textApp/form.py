from django import forms
from textApp.models import UserInfo


class MyForm(forms.ModelForm):
    address = UserInfo
    sex = UserInfo