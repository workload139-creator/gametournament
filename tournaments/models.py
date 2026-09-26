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
