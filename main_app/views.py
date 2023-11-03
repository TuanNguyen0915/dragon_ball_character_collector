from django.shortcuts import render
from django.http import HttpResponse


class Character:
    def __init__(self, name, skill, description):
        self.name = name
        self.skill = skill
        self.description = description


characters = [
    Character(
        "Goku",
        "Kamehameha",
        "Goku's signature attack. A powerful Ki blast fired with two hands after concentrating a large amount of Ki.",
    ),
    Character(
        "Vegeta",
        "Galick Gun",
        "Vegeta's signature technique. Vegeta curls his fingers and places both his hands together at chest level facing the same direction (so that the palm of one hand is on the back of the other).",
    ),
    Character(
        "Frieza",
        "Dealth Beam",
        "To perform the technique, the user extends his right arm and fires a small, thin, very fast and concentrated laser-like beam of ki from his index finger, which barrels down and pierces through the opponent.",
    ),
    Character(
        "Frieza",
        "Dealth Beam",
        "To perform the technique, the user extends his right arm and fires a small, thin, very fast and concentrated laser-like beam of ki from his index finger, which barrels down and pierces through the opponent.",
    ),
]


# Create your views here.
def home(request):
    return HttpResponse("<h1>This is the homepage</h1>")


def about(request):
    return render(request, "about.html")


def character_index(request):
    return render(request, "characters/index.html", {"chars": characters})
