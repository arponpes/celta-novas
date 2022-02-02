from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import ArticleListView, ArticlesMetricsView

schema_view = get_schema_view(
    openapi.Info(
        title="Celta novas API",
        default_version="v1",
        description="Celta novas API",
        terms_of_service="https://opensource.org/licenses/MIT",
        contact=openapi.Contact(email="aronpes94@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("articles", cache_page(15 * 30)(ArticleListView.as_view()), name="articles"),
    path("articles_metrics", ArticlesMetricsView.as_view(), name="articles_metrics"),
    re_path(r"^documentation(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^documentation/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
