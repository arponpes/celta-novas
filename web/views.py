from django.views.generic import ListView

from core.models import Article


class HomePageView(ListView):
    template_name = "web/index.html"
    paginate_by = 10
    model = Article
    queryset = Article.objects.all().order_by('-created_at')[:20]
