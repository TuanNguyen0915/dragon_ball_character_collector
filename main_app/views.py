from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Character


# Create your views here.


class CreateCharacter(CreateView):
    model = Character
    fields = ["name", "skill", "description"]
    success_url = "/characters"


class UpdateCharacter(UpdateView):
    model = Character
    fields = ["name", "skill", "description"]


class DeleteCharacter(DeleteView):
    model = Character
    success_url = "/characters"


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
