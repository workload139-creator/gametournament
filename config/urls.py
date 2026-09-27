from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Admin Panel
    path("admin/", admin.site.urls),

    # Apps
    path("", include("tournaments.urls")),
    path("accounts/", include("accounts.urls")),
    path("teams/", include("teams.urls")),
    path("payments/", include("payments.urls")),
    path("wallet/", include("wallet.urls")),
    path("leaderboard/", include("leaderboard.urls")),
    path("referrals/", include("referrals.urls")),

]

# Media Files
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# Static Files (Development)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
