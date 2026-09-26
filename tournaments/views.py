from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tournament, Registration
from notifications.whatsapp import send_whatsapp

def home(request):
    tournaments = Tournament.objects.all()
    return render(request, "home.html", {
        "tournaments": tournaments
    })

@login_required
def tournament_detail(request, id):

    tournament = get_object_or_404(Tournament, id=id)

    registration = Registration.objects.filter(
        tournament=tournament,
        player=request.user
    ).first()

    return render(request, "tournament_detail.html", {
        "tournament": tournament,
        "registration": registration
    })

@login_required
def register_tournament(request, id):

    tournament = get_object_or_404(Tournament, id=id)

    registration, created = Registration.objects.get_or_create(
        tournament=tournament,
        player=request.user
    )

    return redirect("tournament_detail", id=id)

@login_required
def unlock_room(request, id):

    tournament = get_object_or_404(Tournament, id=id)

    registration = get_object_or_404(
        Registration,
        tournament=tournament,
        player=request.user
    )

    if registration.paid:

        send_whatsapp(
            request.user.phone,
            f"""🔥 FF Tournament

Room ID: {tournament.room_id}

Password: {tournament.room_password}

Good Luck!"""
        )

    return redirect("tournament_detail", id=id)
