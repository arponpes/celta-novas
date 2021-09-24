from django.db.models import Count
from datetime import datetime, timedelta
from django.views.generic import ListView

from core.models import Article


# Burn this function to the ground
class HomePageView(ListView):
    template_name = "web/index.html"
    paginate_by = 10
    model = Article
    queryset = Article.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        articles = Article.objects.all()
        context['total_articles'] = articles.all().count()
        context['articles_last_24_hours'] = articles.filter(
            created_at__gte=datetime.now() - timedelta(hours=24)
        ).count()

        source_with_more_articles_general = None
        number_of_articles = 0
        for a in articles.values('source').annotate(Count('source')):
            if a['source__count'] > number_of_articles:
                source_with_more_articles_general = a['source']
                number_of_articles = a['source__count']
        context['source_with_more_articles_general'] = {
            'source': source_with_more_articles_general,
            'number_of_articles': number_of_articles
        }

        source_with_more_articles = None
        number_of_articles = 0
        for a in articles.filter(
            created_at__gte=datetime.now() - timedelta(hours=24)
        ).values('source').annotate(Count('source')):
            if a['source__count'] > number_of_articles:
                source_with_more_articles = a['source']
                number_of_articles = a['source__count']
        context['source_with_more_articles'] = {
            'source': source_with_more_articles,
            'number_of_articles': number_of_articles
        }
        return context
