
from django.db import models
from django.conf import settings

class MatchResult(models.Model):

    player=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    kills=models.PositiveIntegerField(default=0)

    placement=models.PositiveIntegerField(default=0)

    approved=models.BooleanField(default=False)

    created=models.DateTimeField(auto_now_add=True)

    @property
    def placement_bonus(self):

        table={
            1:100,
            2:50,
            3:25
        }

        return table.get(self.placement,0)

    @property
    def reward(self):

        return (self.kills*5)+self.placement_bonus
