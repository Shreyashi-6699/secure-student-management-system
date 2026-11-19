

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm


def register_view(request):
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
            return redirect("student_list")
        else:
            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("accounts:login")

    return redirect("student_list")
  

# Account views will be implemented here.
