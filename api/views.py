from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from core.models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter
import django_filters
from django.db.models import Count


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = ArticleFilter


class ArticlesMetricsView(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        articles_metrics = {}

        articles_metrics['total_articles'] = articles.count()

        articles_metrics['articles_last_24_hours'] = articles.filter(
            created_at__gt=timezone.now() - timedelta(hours=24)
        ).count()
        # TODO fix case no articles
        articles_metrics['source_with_more_articles'] = articles.values(
            'source'
        ).annotate(
            Count('source')
        ).order_by('-source__count')[0]

        articles_metrics['source_with_more_articles'] = articles.values(
            'source'
        ).annotate(
            Count('source')
        ).order_by('-source__count')[0]

        articles_metrics['source_with_more_articles_last_24_hours'] = \
            articles.filter(
                created_at__gte=timezone.now() - timedelta(hours=24)
            ).values(
                'source'
            ).annotate(
                Count('source')
            ).order_by('-source__count')[0]

        return Response(articles_metrics)
