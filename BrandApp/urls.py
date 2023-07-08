from unicodedata import category
from django.urls import path 
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from BrandApp import views

urlpatterns = [
    path('' , views.landing , name ="landing"),
    path('home/',views.home , name="home" ),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('social-auth/', include('social_django.urls', namespace='social')),
    #path('accounts',include('allauth.urls')),
    #path('oauth/', include('social_django.urls',namespace='social')),
    path('accounts/facebook/login/callback/', views.facebook_callback, name='facebook_callback'),

 

]


