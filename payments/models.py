from django.db import models
from django.conf import settings
from tournaments.models import Tournament

class Payment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True)

    verified = models.BooleanField(default=False)
