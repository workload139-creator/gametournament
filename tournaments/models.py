from django.db import models
from django.conf import settings

class Tournament(models.Model):

    STATUS = (
        ("Upcoming","Upcoming"),
        ("Live","Live"),
        ("Completed","Completed"),
    )

    title = models.CharField(max_length=120)
    entry_fee = models.PositiveIntegerField(default=0)
    prize_pool = models.PositiveIntegerField(default=0)
    date = models.DateTimeField()

    room_id = models.CharField(max_length=50, blank=True)
    room_password = models.CharField(max_length=50, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Upcoming"
    )

    def __str__(self):
        return self.title


class Registration(models.Model):

    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE
    )

    paid = models.BooleanField(default=False)

    order_id = models.CharField(
        max_length=100,
        blank=True
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("player","tournament")
