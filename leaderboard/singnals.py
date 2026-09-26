from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MatchResult

@receiver(post_save,sender=MatchResult)

def reward_player(sender,instance,created,**kwargs):

    if instance.approved:

        instance.player.add_reward(instance.reward)
