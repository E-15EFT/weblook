from django.urls import path
from . import views

urlpatterns = [
    path("homet", views.homet, name="home"),
    path("play-movie/<slug:slug>/", views.play_movie, name="play"),
    path("add-movie/", views.add_movie, name="add-movie"),
]
