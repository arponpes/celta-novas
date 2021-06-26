from django.views.generic.base import TemplateView

from core.models import Article


class HomePageView(TemplateView):

    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marca_articles'] = Article.objects.filter(
            source=Article.MARCA
        ).order_by('-created_at')[:7]
        context['vg_articles'] = Article.objects.filter(
            source=Article.LA_VOZ_DE_GALICIA
        ).order_by('-created_at')[:7]
        context['mc_articles'] = Article.objects.filter(
            source=Article.MOI_CELESTE
        ).order_by('-created_at')[:7]
        context['fv_articles'] = Article.objects.filter(
            source=Article.FARO_DE_VIGO
        ).order_by('-created_at')[:7]
        return context
