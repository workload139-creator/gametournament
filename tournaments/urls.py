from django.urls import path

from .views import (
    home,
    tournament_detail,
    register_tournament,
    unlock_room
)

urlpatterns = [
    path("", home, name="home"),
    path("<int:id>/", tournament_detail, name="tournament_detail"),
    path("register/<int:id>/", register_tournament, name="register_tournament"),
    path("unlock/<int:id>/", unlock_room, name="unlock_room"),
]
