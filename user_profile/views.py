from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username} oy asiye asiye')
        return redirect('home_view')
    context = dict()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username , password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Login oldunuz')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)