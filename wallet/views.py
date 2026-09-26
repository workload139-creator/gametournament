from django.shortcuts import render
from .models import WalletTransaction

def wallet(request):

    tx = WalletTransaction.objects.filter(user=request.user)

    return render(request,"dashboard.html",{
        "transactions":tx
    })
