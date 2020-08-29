from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('create_player', views.PlayerCreate.as_view(), name='player_form'),
]