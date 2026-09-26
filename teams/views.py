from django.shortcuts import render, redirect
from .models import Team

def create_team(request):

    if request.method == "POST":

        Team.objects.create(
            name=request.POST["name"],
            captain=request.user
        )

        return redirect("home")

    return render(request,"create_team.html")
