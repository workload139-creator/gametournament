from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

path("admin/",admin.site.urls),

path("",include("tournaments.urls")),

path("accounts/",include("accounts.urls")),

path("teams/",include("teams.urls")),

path("payments/",include("payments.urls")),

path("wallet/",include("wallet.urls")),

path("leaderboard/",include("leaderboard.urls")),

path("referrals/",include("referrals.urls")),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


from accounts.otp_views import otp_login, verify_otp

urlpatterns += [
    path("accounts/otp/", otp_login, name="otp_login"),
    path("accounts/verify/", verify_otp, name="verify_otp"),
]
