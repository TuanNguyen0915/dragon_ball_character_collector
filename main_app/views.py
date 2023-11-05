from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# models
from .models import Character


# Create your views here.


class CreateCharacter(LoginRequiredMixin, CreateView):
    model = Character
    fields = ["name", "skill", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateCharacter(LoginRequiredMixin, UpdateView):
    model = Character
    fields = ["name", "skill", "description"]


class DeleteCharacter(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = "/characters"


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


@login_required
def character_index(request):
    chars = Character.objects.filter(user=request.user)
    return render(request, "characters/index.html", {"chars": chars})


@login_required
def character_detail(request, char_id):
    character = Character.objects.get(id=char_id)
    return render(request, "characters/detail.html", {"char": character})


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("character-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
