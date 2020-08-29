from django.shortcuts import render

from django.views.generic.base import TemplateView

from .models import Player

class LandingPageView(TemplateView):

    template_name = "landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        return context
