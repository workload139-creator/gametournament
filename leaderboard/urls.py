from django.urls import path

from .views import (
    leaderboard,
    admin_dashboard
)

urlpatterns = [

    path("", leaderboard, name="leaderboard"),

    path(
        "admin-dashboard/",
        admin_dashboard,
        name="admin_dashboard"
    ),

]
