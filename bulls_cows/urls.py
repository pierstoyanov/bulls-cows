from django.contrib import admin
from django.urls import include, path
from bulls_cows import views

urlpatterns = [

    path("", views.home, name="home"),
    path("play/", views.play, name="play"),
]

