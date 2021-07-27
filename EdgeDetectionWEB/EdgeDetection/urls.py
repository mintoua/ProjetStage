"""EdgeDetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import  static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home_view"),
    path('download/', views.download_view, name="download_view"),
    url(r'^/download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    path('contact/', views.contact_view, name="contact_view"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
