from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm
from .models import Category, Tag, Post
import json
from django.contrib import messages

login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form=PostModelForm()
   
    if request.method == 'POST':
        form=PostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f=form.save(commit=False)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value'))
                f.tag.add(tag_item)
            messages.success(request, " Blog postunuz başarıyla kaydedildi. ")
            return redirect('home_view')

    context = dict(
        form = form
     )
    return render(request, 'blog/create_blog_post.html', context)