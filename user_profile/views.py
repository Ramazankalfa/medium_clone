from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from slugify import slugify
from .forms import ProfileModelForm

@login_required(login_url='user:login_view')
def profile_edit_view(request):
    user = request.user
    form = ProfileModelForm(instance=user.profile)
    title = "Profili Düzenle :"
    context = dict(
        form = form,
        title = title,
    )
    return render(request, 'blog/form.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username} daha önce login olmuşsunuz.')
        return redirect('home_view')

    context = dict()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(username) < 6 or len(password) < 6:
              messages.success(request, f'Lütfen kullanıcı adınızı veya şifrenizi doğru giriniz. Kullanıcı adı ve şifreniz 6 karakterden küçük olmamalıdır.')
              return redirect('user_profile:login_view')
              
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Login oldunuz')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)


def logout_view(request):
    messages.success(request, f'{request.user.username} Oturumun kapatıldı.')
    logout(request)
    return redirect('home_view')


def register_view(request):
    context = dict()
    if request.method == 'POST':
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')

        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password) < 3:
            messages.warning(request, "Bilgiler en az 3 karakterden oluşmalıdır...")
            return redirect('user_profile:register_view')

        if email != email_confirm:
            messages.warning(request, "lütfen email bilgilerini doğru giriniz.")
            return redirect('user_profile:register_view')

        if password != password_confirm:
            messages.warning(request, "Lütfen şifre bilgilerini doğru giriniz..")
            return redirect('user_profile:register_view')

        user, created = User.objects.get_or_create(username=email)
        if not created:
            user_login = authenticate(request, username=email, password=password)
            if user is not None:
                messages.success(request, "Daha önce kayıt olmuşsunuz.. Ana sayfaya yönlendiriliyorsunuz.")
                login(request, user_login)
                return redirect('home_view')
            messages.warning(request, f'{email} adresi sistemde kayıtlı ama login olamadınız.. Login sayfasına yönlendiriliyorsunuz.')
            return redirect('user_profile:login_view')
        user.email =email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)

        profile, profile_created = Profile.objects.get_or_create(user=user)
        profile.instagram = instagram
        profile.slug = slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        messages.success(request, f'{user.first_name} Sisteme kaydedildiniz.')
        user_login= authenticate(request, username=email, password=password)
        login(request, user_login)
        return redirect('home_view')
    return render(request, 'user_profile/register.html', context)