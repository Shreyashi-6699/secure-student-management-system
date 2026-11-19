
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import RegistrationForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("student_list")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Account created successfully. Please login."
            )

            return redirect("accounts:login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "registration.html",
        {"form": form}
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("student_list")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            next_url = request.POST.get("next")

            if next_url and next_url.startswith("/"):
                return redirect(next_url)

            return redirect("student_list")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(request, "login.html")


@login_required
@require_POST
def logout_view(request):
    logout(request)

    messages.success(
        request,
        "You have logged out successfully."
    )

    return redirect("accounts:login")
    
