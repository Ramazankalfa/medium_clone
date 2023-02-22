from django.shortcuts import render, get_object_or_404
from blog.models import Post
from user_profile.models import Profile

def all_posts_view(request, user_slug):
    profile = get_object_or_404(Profile, slug=user_slug)
    context=dict(
        posts=Post.objects.filter(user=profile.user, is_active=True)
    )
    return render(request, 'read/all_post.html', context)