from django.db import models
from django.conf import settings

class Referral(models.Model):

    referrer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="referrer"
    )

    referred = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="referred"
    )

    bonus = models.IntegerField(default=20)

    created = models.DateTimeField(auto_now_add=True)
