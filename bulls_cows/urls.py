from django.urls import path
from bulls_cows import views

urlpatterns = [
    path("", views.home, name="home"),
]