from django.shortcuts import render


def home_view(request):
    context =dict()
    return render(request, 'page/home_page.html', context)