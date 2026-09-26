from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]
path("register/<int:id>/",register_tournament,name="register_tournament"),
