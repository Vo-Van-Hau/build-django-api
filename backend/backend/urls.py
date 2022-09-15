"""backend URL Configuration

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
from re import template
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers   
from users import views as user_view

router = routers.DefaultRouter()                   
router.register(r'users', user_view.UsersView, 'users') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('blog/', include('blog.urls')),
    path('signup/', user_view.signup, name = 'signup'),  
    path('signin/', auth_views.LoginView.as_view(template_name = 'signin.html'), name = 'signin'), 
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'), 
]
