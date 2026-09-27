from decimal import Decimal

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MatchResult


@receiver(post_save, sender=MatchResult)
def reward_player(sender, instance, created, **kwargs):
    """
    Approved match result hone par player ko reward wallet me add karta hai.
    Reward ek hi baar diya jayega.
    """

    if not instance.approved:
        return

    if instance.reward_sent:
        return

    reward_amount = Decimal(str(instance.reward))

    if reward_amount <= 0:
        instance.reward_sent = True
        MatchResult.objects.filter(
            pk=instance.pk,
            reward_sent=False
        ).update(reward_sent=True)
        return

    player = instance.player

    # Wallet credit
    player.add_wallet(reward_amount)

    # Transaction record
    from wallet.models import WalletTransaction

    WalletTransaction.objects.create(
        user=player,
        amount=reward_amount,
        transaction_type="Reward"
    )

    # Prevent duplicate reward
    MatchResult.objects.filter(
        pk=instance.pk,
        reward_sent=False
    ).update(
        reward_sent=True
    )
