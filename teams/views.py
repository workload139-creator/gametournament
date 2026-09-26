from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Team

@login_required
def create_team(request):

    if request.method=="POST":

        Team.objects.create(
            name=request.POST["name"],
            captain=request.user
        )

        return redirect("dashboard")

    return render(request,"create_team.html")
