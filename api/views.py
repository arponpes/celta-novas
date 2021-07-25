from rest_framework.generics import ListAPIView
from core.models import Article
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
