from django.views.generic.base import TemplateView

from core.models import New


class HomePageView(TemplateView):

    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marca_news'] = New.objects.filter(
            source='MR'
        ).order_by('-created_at')[:7]
        context['vg_news'] = New.objects.filter(
            source='VG'
        ).order_by('-created_at')[:7]
        context['mc_news'] = New.objects.filter(
            source='MC'
        ).order_by('-created_at')[:7]
        context['fv_news'] = New.objects.filter(
            source='FV'
        ).order_by('-created_at')[:7]
        return context
