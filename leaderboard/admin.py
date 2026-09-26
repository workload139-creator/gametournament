from django.contrib import admin
from .models import MatchResult

@admin.register(MatchResult)

class MatchAdmin(admin.ModelAdmin):

    list_display=(
        "player",
        "kills",
        "placement",
        "approved"
    )

    list_editable=("approved",)
