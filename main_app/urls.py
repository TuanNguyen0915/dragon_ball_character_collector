from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("characters/", views.character_index, name="character-index"),
    # CRUD character
    path("characters/<int:char_id>/", views.character_detail, name="character-detail"),
    path(
        "characters/create/", views.CreateCharacter.as_view(), name="create-character"),
]
