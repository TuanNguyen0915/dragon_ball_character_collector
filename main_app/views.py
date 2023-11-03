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


def character_detail(request, char_id):
    character = Character.objects.get(id=char_id)
    return render(request, "characters/detail.html", {"char": character})
