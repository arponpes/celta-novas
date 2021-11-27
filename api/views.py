from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from core.models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter
import django_filters
from .helpers.article_metrics_generator import ArticleMetricsGenerator


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = ArticleFilter


class ArticlesMetricsView(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        article_metrics_generator = ArticleMetricsGenerator(articles)
        article_metrics = article_metrics_generator()

        return Response(article_metrics)
