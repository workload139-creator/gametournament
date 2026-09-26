from django.db import models

class Tournament(models.Model):

    title = models.CharField(max_length=100)
    entry_fee = models.PositiveIntegerField()
    prize_pool = models.PositiveIntegerField()
    date = models.DateTimeField()

    room_id = models.CharField(max_length=50, blank=True)
    room_password = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
from django.conf import settings

class Registration(models.Model):

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    paid = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
