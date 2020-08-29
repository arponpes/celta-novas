from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
]