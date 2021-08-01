from rest_framework.generics import ListAPIView
from core.models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter
import django_filters


class ArticleListView(ListAPIView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = ArticleFilter
