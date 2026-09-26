from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Tournament, Registration

def home(request):

    tournaments = Tournament.objects.all()

    return render(request, "home.html", {
        "tournaments": tournaments
    })


@login_required
def register_tournament(request, id):

    tournament = get_object_or_404(
        Tournament,
        id=id
    )

    Registration.objects.get_or_create(
        tournament=tournament,
        player=request.user
    )

    return redirect("dashboard")


@login_required
def tournament_detail(request, id):

    tournament = get_object_or_404(
        Tournament,
        id=id
    )

    registration = Registration.objects.filter(
        tournament=tournament,
        player=request.user
    ).first()

    return render(
        request,
        "tournament_detail.html",
        {
            "tournament": tournament,
            "registration": registration,
        }
    )
