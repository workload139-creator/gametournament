from django.db import models
from django.conf import settings

class WalletTransaction(models.Model):

    TYPE = (
        ("Reward", "Reward"),
        ("Withdraw", "Withdraw"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TYPE
    )

    created = models.DateTimeField(auto_now_add=True)


class WithdrawRequest(models.Model):

    STATUS = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    upi_id = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    created = models.DateTimeField(auto_now_add=True)
