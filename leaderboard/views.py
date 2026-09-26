from django.shortcuts import render
from .models import MatchResult

def leaderboard(request):

    results = MatchResult.objects.all()

    return render(request, "leaderboard.html", {
        "results": results
    })
