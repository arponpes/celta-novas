from django.views.generic.base import TemplateView

from core.models import New

class HomePageView(TemplateView):

    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = New.objects.all().order_by('-created_at')[:5]
        return context
