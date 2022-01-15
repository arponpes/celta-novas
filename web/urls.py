from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path(
        '',
        cache_page(15 * 30)(views.HomePageView.as_view()),
        name='home'
    )
]
