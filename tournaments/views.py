from django.shortcuts import render
from .models import Tournament

def home(request):

    tournaments = Tournament.objects.all()

    return render(request, "home.html", {
        "tournaments": tournaments
    })
