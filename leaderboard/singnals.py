from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MatchResult
from wallet.models import WalletTransaction
from notifications.whatsapp import send_whatsapp

@receiver(post_save,sender=MatchResult)

def reward_player(sender,instance,created,**kwargs):

    if instance.approved and not instance.reward_sent:

        instance.player.add_reward(instance.reward)

        WalletTransaction.objects.create(

            user=instance.player,

            amount=instance.reward,

            transaction_type="Tournament Reward"

        )

        send_whatsapp(

            instance.player.whatsapp_number(),

            f"""🏆 Reward Added

Kills: {instance.kills}

Reward: ₹{instance.reward}

Wallet Updated Successfully."""

        )

        instance.reward_sent=True

        instance.save()
