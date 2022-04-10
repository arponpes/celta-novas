from datetime import date

from core.models import Article
from core.tests.factories import ArticleFactory
from django.urls.base import reverse
from rest_framework.test import APIClient

import pytest


@pytest.mark.django_db
def test_get_articles():
    article_1 = ArticleFactory()
    article_2 = ArticleFactory()
    expected_results = [
        {
            "title": article_1.title,
            "url": article_1.url,
            "source": article_1.source,
            "image_url": article_1.image_url,
            "created_at": article_1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        },
        {
            "title": article_2.title,
            "url": article_2.url,
            "source": article_2.source,
            "image_url": article_2.image_url,
            "created_at": article_2.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        },
    ]
    expected_response = {"count": 2, "next": None, "previous": None, "results": expected_results}
    client = APIClient()
    response = client.get(reverse("articles"))
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_post_article():
    article = ArticleFactory()
    data = {
        "title": article.title,
        "url": article.url,
        "source": article.source,
        "created_at": article.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    }
    client = APIClient()
    response = client.post(reverse("articles"), data)
    assert response.status_code == 405
    assert response.json() == {"detail": 'Method "POST" not allowed.'}


@pytest.mark.django_db
def test_get_articles_filtered():
    article_1 = ArticleFactory(source=Article.FARO_DE_VIGO)
    ArticleFactory(source=Article.MARCA)
    expected_results = [
        {
            "title": article_1.title,
            "url": article_1.url,
            "source": article_1.source,
            "image_url": article_1.image_url,
            "created_at": article_1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }
    ]
    expected_response = {"count": 1, "next": None, "previous": None, "results": expected_results}
    client = APIClient()
    response = client.get(reverse("articles"), data={"source": Article.FARO_DE_VIGO})
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_get_articles_filtered_incorrect_source():
    ArticleFactory(source=Article.FARO_DE_VIGO)
    ArticleFactory(source=Article.MARCA)
    expected_response = {"source": ["Select a valid choice. foo is not one of the available choices."]}
    client = APIClient()
    response = client.get(reverse("articles"), data={"source": "foo"})
    assert response.status_code == 400
    assert response.json() == expected_response


@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.django_db
def test_get_articles_metrics():
    ArticleFactory(source=Article.FARO_DE_VIGO)
    ArticleFactory(source=Article.MARCA)
    ArticleFactory(source=Article.MARCA)
    old_article = ArticleFactory(source=Article.MARCA)
    old_article.created_at = date(2020, 1, 1)
    old_article.save()
    expected_response = {
        "total_articles": 4,
        "articles_last_24_hours": 3,
        "source_with_more_articles": {"source": "MARCA", "source__count": 3},
        "source_with_more_articles_last_24_hours": {"source": "MARCA", "source__count": 2},
        "articles_by_source": {
            Article.FARO_DE_VIGO: 1,
            Article.LA_VOZ_DE_GALICIA: 0,
            Article.MARCA: 3,
            Article.FARO_DE_VIGO: 0,
        },
        "articles_last_week_by_date": [{"created_at__date": date(2022, 4, 3), "count": 3}],
        "articles_last_week_by_date_by_source": {
            "MARCA": {"created_at__date": date(2022, 4, 10), "count": 2},
            "MOI CELESTE": [],
            "LA VOZ DE GALICIA": [],
            "FARO DE VIGO": [{"created_at__date": date(2022, 4, 10), "count": 1}],
        },
    }
    client = APIClient()
    response = client.get(reverse("articles_metrics"))
    assert response.status_code == 200
    assert response.data == expected_response
