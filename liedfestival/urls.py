"""liedfestival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import os.path

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from django.views.generic import TemplateView
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
    path('motto/', views.letmesee, {'tag': 'motto'}),
    path('pianovoceensemble/', views.letmesee, {'tag': 'pianovoceensemble'}),
    path('konzerte/', views.letmesee, {'tag': 'konzerte'}),
    path('workshop/', views.letmesee, {'tag': 'workshop'}),
    path('jungepreisträger', views.letmesee, {'tag': 'jungepreistraeger'}),
    # path('förderer/', views.letmesee, {'tag': 'foerderer'}),
    # path('sponsoren/', views.letmesee, {'tag': 'foerderer'}),
    path('karten/', views.karten),
    path('workshop-anmeldung/', views.workshop_anmeldung),
    path('favicon.ico', views.favicon),
    path('googleba5118c5e56500e9.html', views.google),
    path('', views.index)
]

if os.path.isfile('./liedfestival/.local'):
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
