from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, View

from core.metrics.article_metrics_generator import ArticleMetricsGenerator
from core.models import Article


class HomePageView(ListView):
    template_name = "web/index.html"
    paginate_by = 10
    model = Article
    queryset = Article.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        articles = Article.objects.all()
        article_metrics_generator = ArticleMetricsGenerator(articles)
        article_metrics = article_metrics_generator()
        context["article_metrics"] = article_metrics
        return context


class StatsPageView(TemplateView):
    template_name = "web/stats.html"


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "OK"}, status=200)
