from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "database/index.html")


def login_view(request):
    if request.method == "POST":
        user = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "database/login.html")
    return render(request, "database/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
