from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm
from .models import Category, Tag, Post

login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form=PostModelForm()
    context = dict(
        form = form
    )
    if request.method == 'POST':
        form=PostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f=form.save(commit=False)
            f.user = request.user
            f.save()
            print(form.cleaned_data)
    return render(request, 'blog/create_blog_post.html', context)