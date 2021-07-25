from core.tests.factories import ArticleFactory
from rest_framework.test import APIClient
from django.urls.base import reverse
import pytest


@pytest.mark.django_db
def test_get_articles():
    article_1 = ArticleFactory()
    article_2 = ArticleFactory()
    expected_response = [
        {
            'title': article_1.title,
            'url': article_1.url,
            'source': article_1.source,
            'created_at': article_1.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%fZ'
            )
        }, {
            'title': article_2.title,
            'url': article_2.url,
            'source': article_2.source,
            'created_at': article_2.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%fZ'
            )
        }
    ]
    client = APIClient()
    response = client.get(reverse('articles'))
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_post_article():
    article = ArticleFactory()
    data = {
            'title': article.title,
            'url': article.url,
            'source': article.source,
            'created_at': article.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%fZ'
            )
        }
    client = APIClient()
    response = client.post(reverse('articles'), data)
    assert response.status_code == 405
    assert response.json() == {'detail': 'Method "POST" not allowed.'}
