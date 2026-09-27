from django.shortcuts import render
from .models import MatchResult

def leaderboard(request):

    results=MatchResult.objects.filter(
        approved=True
    ).order_by("-kills","placement")

    return render(
        request,
        "leaderboard.html",
        {
            "results":results
        }
    )
