from django.db import models

class MatchResult(models.Model):

    team = models.CharField(max_length=50)
    kills = models.IntegerField(default=0)
    placement = models.IntegerField(default=0)

    @property
    def points(self):

        table = {
            1: 12,
            2: 9,
            3: 8,
            4: 7,
            5: 6
        }

        return self.kills + table.get(self.placement, 0)
