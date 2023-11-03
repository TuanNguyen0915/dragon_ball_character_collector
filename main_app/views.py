from django.shortcuts import render
from .models import Character


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def character_index(request):
    chars = Character.objects.all()
    return render(request, "characters/index.html", {"chars": chars})
