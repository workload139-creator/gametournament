from django.http import HttpResponse
from django.urls import path


def referral_home(request):
    return HttpResponse("FF Tournament Pro Referral System")


urlpatterns = [
    path("", referral_home, name="referral_home"),
]
