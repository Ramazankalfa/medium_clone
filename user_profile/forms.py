from django import forms
from .models import Profile
from tinymce.widgets import TinyMCE
from django.core import validators


class ProfileModelForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Profile
        fields =[
            'first_name',
            'last_name',
            'avatar',
            'instagram',
            'info',
        ]