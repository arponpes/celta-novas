from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

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
