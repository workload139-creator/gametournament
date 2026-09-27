import csv
from io import TextIOWrapper

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import MatchResult
from .forms import CSVUploadForm
from accounts.models import User
from tournaments.models import Tournament

@login_required
def leaderboard(request):
    results = MatchResult.objects.filter(
        approved=True
    ).order_by("-kills", "placement")

    return render(request, "leaderboard.html", {
        "results": results
    })


@login_required
def admin_dashboard(request):

    form = CSVUploadForm()

    if request.method == "POST":

        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():

            file = TextIOWrapper(
                request.FILES["file"].file,
                encoding="utf-8"
            )

            reader = csv.DictReader(file)

            tournament = Tournament.objects.last()

            for row in reader:

                user = User.objects.filter(
                    username=row["username"]
                ).first()

                if user:

                    MatchResult.objects.create(
                        player=user,
                        tournament=tournament,
                        kills=int(row["kills"]),
                        placement=int(row["placement"]),
                        approved=True
                    )

            return redirect("admin_dashboard")

    return render(request, "admin_dashboard.html", {
        "form": form,
        "total_players": User.objects.count(),
        "total_tournaments": Tournament.objects.count(),
        "revenue": 0,
        "payout": 0
    })
