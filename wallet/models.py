from django.db import models
from django.conf import settings

class WalletTransaction(models.Model):

    TYPE=(
        ("Tournament Reward","Tournament Reward"),
        ("Withdraw","Withdraw"),
        ("Deposit","Deposit"),
    )

    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_type=models.CharField(
        max_length=30,
        choices=TYPE
    )

    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
