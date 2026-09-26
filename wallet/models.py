from django.db import models
from django.conf import settings

class WalletTransaction(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_type = models.CharField(
        max_length=20
    )

    created = models.DateTimeField(auto_now_add=True)
