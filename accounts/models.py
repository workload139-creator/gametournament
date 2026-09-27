from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

class User(AbstractUser):
    # Free Fire Details
    ff_uid = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Free Fire UID"
    )

    phone = models.CharField(
        max_length=15,
        unique=True
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    # Wallet
    wallet = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_kills = models.PositiveIntegerField(default=0)
    total_matches = models.PositiveIntegerField(default=0)
    total_wins = models.PositiveIntegerField(default=0)

    # Referral
    referral_code = models.CharField(
        max_length=10,
        unique=True,
        blank=True
    )

    referred_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="referrals"
    )

    # Verification
    phone_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = get_random_string(
                8,
                allowed_chars="ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
            )
        super().save(*args, **kwargs)

    def add_wallet(self, amount):
        self.wallet += amount
        self.save(update_fields=["wallet"])

    def deduct_wallet(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount
            self.save(update_fields=["wallet"])
            return True
        return False

    def add_match_result(self, kills=0, win=False):
        self.total_matches += 1
        self.total_kills += kills
        if win:
            self.total_wins += 1
        self.save(update_fields=[
            "total_matches",
            "total_kills",
            "total_wins"
        ])

    @property
    def kd_ratio(self):
        if self.total_matches == 0:
            return 0
        return round(self.total_kills / self.total_matches, 2)

    @property
    def win_rate(self):
        if self.total_matches == 0:
            return 0
        return round((self.total_wins / self.total_matches) * 100, 2)

    def whatsapp_number(self):
        return self.phone.replace("+", "")

    def __str__(self):
        return f"{self.username} ({self.ff_uid})"
