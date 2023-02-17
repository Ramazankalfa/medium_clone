from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
        print('*' * 30)
        print(email,email_confirm,first_name,last_name,password,password_confirm,instagram)
        print('*' * 30)
    return render(request, 'user_profile/register.html', context)