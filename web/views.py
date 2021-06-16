from django.views.generic.base import TemplateView

from core.models import New


class HomePageView(TemplateView):

    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marca_news'] = New.objects.filter(
            source=New.MARCA
        ).order_by('-created_at')[:7]
        context['lv_news'] = New.objects.filter(
            source=New.LA_VOZ_DE_GALICIA
        ).order_by('-created_at')[:7]
        context['mc_news'] = New.objects.filter(
            source=New.MOI_CELESTE
        ).order_by('-created_at')[:7]
        context['fv_news'] = New.objects.filter(
            source=New.FARO_DE_VIGO
        ).order_by('-created_at')[:7]
        return context
