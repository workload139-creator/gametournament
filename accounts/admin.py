from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)

class CustomUserAdmin(UserAdmin):

    fieldsets=UserAdmin.fieldsets+(
    ("Free Fire",{
    "fields":(
    "ff_uid",
    "phone",
    "wallet"
    )
    }),
    )

    list_display=(
    "username",
    "ff_uid",
    "wallet",
    "is_staff"
    )
