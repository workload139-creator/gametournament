from django import forms

class WithdrawForm(forms.Form):

    upi_id = forms.CharField()

    amount = forms.DecimalField()
