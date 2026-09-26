from django.db import models
from django.conf import settings

class Payment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    order_id = models.CharField(max_length=100)

    payment_id = models.CharField(
        max_length=100,
        blank=True
    )

    amount = models.PositiveIntegerField()

    verified = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
