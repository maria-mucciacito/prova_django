
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('prenotazione/',views.selection_airport, name="selection_airport"),
    path('voli/',views.visualizza_voli, name="visualizza_volo"),
]