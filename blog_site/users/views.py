from django.shortcuts import render, redirect
from users.forms import registerform, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


def register_view(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            if User.objects.filter(username=username).first():
                messages.error(request, "Account already created with this username.")
            else:
                form.save()
                name = form.cleaned_data["name"]
                messages.success(request, f"Account created for {name}")
                return redirect("signin")
    else:
        form = registerform()

    return render(request, "users/register.html", {"form": form})


def signin_view(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password1"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "You are not authorized to login.")
            return redirect("signin")
    else:
        return render(request, "users/signin.html")


@login_required(login_url="home/signin")
def logout_view(request):
    logout(request)
    return redirect("signin")


@login_required(login_url="home/signin")
def profile(request):
    return render(request, "users/profile.html")


@login_required(login_url="home/signin")
def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    print(profile)
    if request.method != "POST":
        form = ProfileUpdateForm(instance=profile)
    else:
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            profile.author = request.user
            profile.profile_image = request.FILES
            return redirect("/profile")
    context = {"profile": profile, "form": form}
    return render(request, "users/edit_profile.html", context)
