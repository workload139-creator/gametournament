from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Free Fire",
            {
                "fields": (
                    "ff_uid",
                    "phone",
                    "wallet",
                    "profile_image",
                    "referral_code",
                    "referred_by",
                    "phone_verified",
                    "email_verified",
                    "total_kills",
                    "total_matches",
                    "total_wins",
                )
            },
        ),
    )

    list_display = (
        "username",
        "ff_uid",
        "phone",
        "wallet",
        "total_kills",
        "total_wins",
        "is_staff",
    )

    search_fields = (
        "username",
        "ff_uid",
        "phone",
    )
