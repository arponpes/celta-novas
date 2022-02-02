import django_filters
from core.models import Article


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ("source",)
