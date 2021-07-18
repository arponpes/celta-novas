from rest_framework.viewsets import ModelViewSet
from core.models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
