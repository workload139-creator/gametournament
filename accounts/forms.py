from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email Address"
        })
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+91XXXXXXXXXX"
        })
    )

    ff_uid = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Free Fire UID"
        })
    )

    referral_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Referral Code (Optional)"
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "ff_uid",
            "referral_code",
            "password1",
            "password2",
        ]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
            })
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                "Phone number already registered."
            )

        return phone

    def clean_ff_uid(self):
        uid = self.cleaned_data["ff_uid"]

        if User.objects.filter(ff_uid=uid).exists():
            raise forms.ValidationError(
                "Free Fire UID already registered."
            )

        return uid

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        user.ff_uid = self.cleaned_data["ff_uid"]

        code = self.cleaned_data.get("referral_code")

        if code:
            try:
                user.referred_by = User.objects.get(
                    referral_code=code.upper()
                )
            except User.DoesNotExist:
                pass

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )
