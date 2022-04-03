from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path("", cache_page(15 * 30)(views.HomePageView.as_view()), name="home"),
    path("stats/", cache_page(15 * 30)(views.StatsPageView.as_view()), name="stats"),
]
