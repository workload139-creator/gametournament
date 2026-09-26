from django.shortcuts import render
from .models import MatchResult

def leaderboard(request):

    data=MatchResult.objects.filter(
        approved=True
    ).order_by("-kills")

    return render(
        request,
        "leaderboard.html",
        {
            "results":data
        }
    )
