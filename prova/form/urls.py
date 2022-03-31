from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name="form"),
    path('create_utente', views.insert_utente, name='create_utente'),
    path('visualizza_utenti', views.visualizza_utenti, name='visualizza_utenti'),
    path('delete_utente/<str:pk>/', views.delete_utente, name='delete_utente'),
    path('update_utente/<str:pk>/', views.update_utente, name='update_utente'),
    path('posti/', views.posti, name='posti'),
]