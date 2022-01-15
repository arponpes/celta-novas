import pytest
from django.core.paginator import Page
from django.urls.base import reverse
from rest_framework.test import APIClient

from core.models import Article
from core.tests.factories import ArticleFactory


@pytest.mark.django_db
def test_get():
    for _ in range(10):
        ArticleFactory()
    articles_expected = Article.objects.all().order_by('-created_at')
    client = APIClient()
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert set(response.context['article_list']) == set(articles_expected)
    assert isinstance(response.context['page_obj'], Page)
