from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import RegisterForm

from .models import Player, POSITIONS, OPINION


class LandingPageView(TemplateView):

    template_name = "fmweb/landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        return context

class PlayerCreate(CreateView):
    model = Player
    fields = [
        'name',
        'position',
        'opinion',
        'notes'
    ]

    success_url = reverse_lazy('landing_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = POSITIONS
        context['opinions'] = OPINION
        return context

def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/fm")
    else:
	    form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})
