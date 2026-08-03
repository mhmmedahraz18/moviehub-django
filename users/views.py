from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration successful! Welcome to MovieHub."
            )

            return redirect("login")

    else:

        form = RegisterForm()

    print(form)
    return render(request, "users/register.html", {"form": form})

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )
        print("Authenticated User:", user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("home")

        messages.error(request, "Invalid Username or Password")

    return render(request, "users/login.html")

def logout_view(request):

    logout(request)

    messages.success(request, "Logged out successfully!")

    return redirect("login")