from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm
def dashboard(request):
    # return render(request, "users/dashboard.html")ВИПРАВИТИ!!!!
    return render(request, "dashboard.html")

def sign_up(request):
    # pass
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(request, "sign_up.html", {"form": form})
def log_in(request):
    pass
def _logout(request):
    pass