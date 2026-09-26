from django.urls import path

from .views import (
    home,
    tournament_detail,
    register_tournament,
    room_unlock
)

urlpatterns = [

    path("",home,name="home"),

    path("<int:id>/",tournament_detail,name="tournament_detail"),

    path("register/<int:id>/",register_tournament,name="register_tournament"),

    path("unlock/<int:id>/",room_unlock,name="room_unlock"),

]
