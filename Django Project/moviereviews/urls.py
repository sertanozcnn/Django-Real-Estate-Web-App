"""moviereviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from zipfile import Path
from django.contrib import admin
from django.urls import path , include
from appSale import views as appSaleViews
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from contacts.views import AdminContactView

urlpatterns =[
    path('admin/', admin.site.urls),
   # path('',appSaleViews.home ,name='home'), 
    path('', appSaleViews.index, name='index'),
    path('', appSaleViews.index, name='indexList'),
    path('about/',appSaleViews.about, name='about'),
    path('house/',appSaleViews.house, name='house'),
    path('price/',appSaleViews.price, name='price'),
    path('contact/',appSaleViews.contact, name='contact'),
   
    path('subscribe/',appSaleViews.subscribe, name='subscribe'),

    #path('signup/',appSaleViews.signup, name='signup'),
    #path('accounts/', include('accounts.urls'))
    path("", include('accounts.urls')),

    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    # path('admin/', admin.site.urls),
    path('admin/contact/', AdminContactView.as_view(), name='admin-contact'),
    
    
     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/auth/password_reset_done.html'),
         name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(  # noqa
        template_name="accounts/auth/password_reset_confirm.html"),
         name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/auth/password_reset_complete.html'),
         name='password_reset_complete'),
    
    
        
]

urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)
