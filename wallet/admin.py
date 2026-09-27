from django.contrib import admin
from .models import WalletTransaction, WithdrawRequest

@admin.register(WalletTransaction)
class WalletAdmin(admin.ModelAdmin):
    list_display=("user","amount","transaction_type","created")

@admin.register(WithdrawRequest)
class WithdrawAdmin(admin.ModelAdmin):
    list_display=("user","amount","upi_id","status")
    list_editable=("status",)
