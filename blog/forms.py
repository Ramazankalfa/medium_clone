from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))


    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'cover_image',
            'category',
            'tag',
        ]