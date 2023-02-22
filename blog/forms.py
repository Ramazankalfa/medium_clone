from django import forms
from .models import Post
from tinymce.widgets import TinyMCE
from django.core import validators


def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Opps. En az 3 karakter olmalıdır... ")

class PostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))
    title = forms.CharField(validators=[min_length_3, ])


    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'cover_image',
            'category',
            'tag',
        ]