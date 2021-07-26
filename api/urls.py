from django.views.decorators.cache import cache_page
from django.urls import path
from .views import ArticleListView


urlpatterns = [
    path(
        'articles',
        cache_page(60 * 30)(ArticleListView.as_view()),
        name='articles'
    ),
]
