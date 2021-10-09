from django.views.decorators.cache import cache_page
from django.urls import path
from .views import ArticleListView, ArticlesMetricsView


urlpatterns = [
    path(
        'articles',
        cache_page(15 * 30)(ArticleListView.as_view()),
        name='articles'
    ),
    path(
        'articles_metrics',
        ArticlesMetricsView.as_view(),
        name='articles_metrics'
    ),
]
