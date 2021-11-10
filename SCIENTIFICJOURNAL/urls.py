"""SCIENTIFICJOURNAL URL Configuration

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
from django.urls import path,include
import debug_toolbar
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('journals/',include('journals.urls')),
    path('manuscripts/',include('manuscript.urls')),
   
     path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/dashboard/',include('dashboards.urls')),
     path('accounts/dashboard/manuscript',include('manuscript.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    
    
  path('',views.home_view,name='home'),
]
