from django.shortcuts import render
from .models import Tournament

def home(request):

    tournaments = Tournament.objects.all()

    return render(request, "home.html", {
        "tournaments": tournaments
    })
from django.shortcuts import get_object_or_404, redirect
from .models import Tournament, Registration

def register_tournament(request,id):

    tournament = get_object_or_404(Tournament,id=id)

    Registration.objects.get_or_create(
        tournament=tournament,
        player=request.user
    )

    return redirect("dashboard")
