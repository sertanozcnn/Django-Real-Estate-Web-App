# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import dashboard,register,logout,login,ProfileUpdateView,password_reset_request

from django.contrib.auth.views import LogoutView
from appSale import views as appSaleViews
from django.contrib.auth.decorators import login_required

from .views import (ProfileUpdateView)

urlpatterns = [
    # path('login/', login_view, name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile/<int:pk>', login_required(
         ProfileUpdateView.as_view()), name='profile'),
    path("password-reset", password_reset_request, name="password-reset")
    
]
