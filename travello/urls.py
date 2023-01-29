from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("home", views.index, name="home"),
               path("travello", views.index, name="travello"),
               path("about", views.about, name="about")]
