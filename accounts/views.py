from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Referral bonus
            if user.referred_by:
                user.referred_by.add_wallet(20)

            login(request, user)

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


@login_required
def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html"
    )


@login_required
def profile_view(request):
    return render(
        request,
        "accounts/profile.html"
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
