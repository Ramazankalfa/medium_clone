from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    tag = forms.CharField()
    
    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'cover_image',
            'category',
            'tag',
        ]