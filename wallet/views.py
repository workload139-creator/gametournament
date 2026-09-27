from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import WithdrawForm
from .models import (
    WalletTransaction,
    WithdrawRequest
)

@login_required
def wallet(request):

    form = WithdrawForm()

    if request.method == "POST":

        form = WithdrawForm(request.POST)

        if form.is_valid():

            amount = form.cleaned_data["amount"]

            if request.user.wallet >= amount:

                WithdrawRequest.objects.create(
                    user=request.user,
                    amount=amount,
                    upi_id=form.cleaned_data["upi_id"]
                )

                request.user.wallet -= amount

                request.user.save()

                WalletTransaction.objects.create(
                    user=request.user,
                    amount=amount,
                    transaction_type="Withdraw"
                )

                return redirect("wallet")

    tx = WalletTransaction.objects.filter(
        user=request.user
    ).order_by("-created")

    return render(request, "wallet.html", {
        "transactions": tx,
        "form": form
    })
