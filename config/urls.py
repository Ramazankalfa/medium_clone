"""config URL Configuration
    https://docs.djangoproject.com/en/4.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from page.views import home_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('user/', include('user_profile.urls', namespace='user')),
    path('read/', include('read.urls', namespace='read')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
