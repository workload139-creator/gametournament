from django.shortcuts import render
from .firebase import firebase_config

def otp_login(request):
    return render(request, "accounts/otp_login.html", {
        "firebase": firebase_config()
    })

def verify_otp(request):
    return render(request, "accounts/verify_otp.html")
