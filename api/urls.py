from django.urls import path
from django.views.decorators.cache import cache_page
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import ArticleListView, ArticlesMetricsView

urlpatterns = [
    path("articles", cache_page(15 * 30)(ArticleListView.as_view()), name="articles"),
    path("articles_metrics", ArticlesMetricsView.as_view(), name="articles_metrics"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
