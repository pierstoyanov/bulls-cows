from django.contrib import admin
from django.urls import include, path

from bulls_cows import views

urlpatterns = [
    path("bulls_cows/<name>", views.hello_there, name="hello_there"),
]