from django.db import models
from django.urls import reverse
 
# Create your models here.

# characters = [
#     Character(
#         "Goku",
#         "Kamehameha",
#         "Goku's signature attack. A powerful Ki blast fired with two hands after concentrating a large amount of Ki.",
#     ),
#     Character(
#         "Vegeta",
#         "Galick Gun",
#         "Vegeta's signature technique. Vegeta curls his fingers and places both his hands together at chest level facing the same direction (so that the palm of one hand is on the back of the other).",
#     ),
#     Character(
#         "Frieza",
#         "Dealth Beam",
#         "To perform the technique, the user extends his right arm and fires a small, thin, very fast and concentrated laser-like beam of ki from his index finger, which barrels down and pierces through the opponent.",
#     ),
#     Character(
#         "Frieza",
#         "Dealth Beam",
#         "To perform the technique, the user extends his right arm and fires a small, thin, very fast and concentrated laser-like beam of ki from his index finger, which barrels down and pierces through the opponent.",
#     ),
# ]


class Character(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"char_id": self.id})
    