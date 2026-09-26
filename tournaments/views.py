from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from .models import Tournament,Registration

from notifications.whatsapp import send_whatsapp

def home(request):

    tournaments = Tournament.objects.all().order_by("date")

    return render(request,"home.html",{
        "tournaments":tournaments
    })

@login_required
def tournament_detail(request,id):

    tournament = get_object_or_404(Tournament,id=id)

    registration = Registration.objects.filter(
        player=request.user,
        tournament=tournament
    ).first()

    return render(request,"tournament_detail.html",{
        "tournament":tournament,
        "registration":registration
    })

@login_required
def register_tournament(request,id):

    tournament = get_object_or_404(Tournament,id=id)

    Registration.objects.get_or_create(
        player=request.user,
        tournament=tournament
    )

    return redirect("tournament_detail",id=id)

@login_required
def room_unlock(request,id):

    tournament = get_object_or_404(Tournament,id=id)

    registration = get_object_or_404(
        Registration,
        player=request.user,
        tournament=tournament
    )

    if registration.paid:

        send_whatsapp(
            request.user.whatsapp_number(),
            f"""🔥 FF Tournament

Tournament: {tournament.title}

Room ID: {tournament.room_id}

Password: {tournament.room_password}

Best of Luck!"""
        )

    return redirect("tournament_detail",id=id)
