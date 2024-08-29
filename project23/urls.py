"""
URL configuration for project23 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('string_byfbv/',string_byfbv,name='string_byfbv'),
    path('StringByCbv/',StringByCbv.as_view(),name='StringByCbv'),

    path('fbvfile/',fbvfile,name='fbvfile'),
    path('CbvFile/',CbvFile.as_view(),name='CbvFile'),

    path('isbyfbv/',isbyfbv,name='isbyfbv'),
    path('ISByCbv/',ISByCbv.as_view(),name='ISByCbv'),




    path('HtmlByTV/',HtmlByTV.as_view(),name='HtmlByTV'),




]







