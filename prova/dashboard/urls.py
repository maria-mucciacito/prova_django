from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/', views.login_user,name='login'),
    path('login/',auth_views.LoginView.as_view(),name='login' ),
    path('logout/',auth_views.LogoutView.as_view(),name='logout' ),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/voli', views.visualizza_voli, name="voli"),


]
    
