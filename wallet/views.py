from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WalletTransaction

@login_required
def wallet(request):

    tx=WalletTransaction.objects.filter(
        user=request.user
    ).order_by("-created")

    return render(
        request,
        "wallet.html",
        {
            "transactions":tx
        }
    )
