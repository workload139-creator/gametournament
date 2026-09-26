from django.db import models
from django.conf import settings

class Team(models.Model):

    name = models.CharField(
        max_length=60,
        unique=True
    )

    captain = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    logo = models.ImageField(
        upload_to="team_logo/",
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("team","player")
