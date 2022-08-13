import datetime
import json
import zoneinfo

import pytest
from django.urls.base import reverse
from freezegun import freeze_time
from rest_framework.test import APIClient

from core.models import Article
from tests.unittest.core.factories import ArticleFactory


@freeze_time("2022-05-21")
@pytest.mark.django_db
def test_get_articles_metrics():
    load_fake_data()
    expected_response = {
        "total_articles": 8242,
        "articles_last_24_hours": 26,
        "source_with_more_articles": {"source": "LA VOZ DE GALICIA", "source__count": 2968},
        "source_with_more_articles_last_24_hours": {"source": "MOI CELESTE", "source__count": 14},
        "articles_by_source": {"MARCA": 883, "MOI CELESTE": 2565, "LA VOZ DE GALICIA": 2968, "FARO DE VIGO": 1826},
        "articles_last_week_by_date": [
            {"created_at__date": datetime.date(2022, 5, 14), "count": 23},
            {"created_at__date": datetime.date(2022, 5, 15), "count": 50},
            {"created_at__date": datetime.date(2022, 5, 16), "count": 29},
            {"created_at__date": datetime.date(2022, 5, 17), "count": 21},
            {"created_at__date": datetime.date(2022, 5, 18), "count": 19},
            {"created_at__date": datetime.date(2022, 5, 19), "count": 24},
            {"created_at__date": datetime.date(2022, 5, 20), "count": 26},
        ],
        "articles_last_week_by_date_by_source": {
            "MARCA": [
                {"created_at__date": datetime.date(2022, 5, 14), "count": 2},
                {"created_at__date": datetime.date(2022, 5, 15), "count": 5},
                {"created_at__date": datetime.date(2022, 5, 16), "count": 3},
                {"created_at__date": datetime.date(2022, 5, 17), "count": 3},
                {"created_at__date": datetime.date(2022, 5, 18), "count": 1},
                {"created_at__date": datetime.date(2022, 5, 19), "count": 1},
                {"created_at__date": datetime.date(2022, 5, 20), "count": 2},
            ],
            "MOI CELESTE": [
                {"created_at__date": datetime.date(2022, 5, 14), "count": 8},
                {"created_at__date": datetime.date(2022, 5, 15), "count": 12},
                {"created_at__date": datetime.date(2022, 5, 16), "count": 9},
                {"created_at__date": datetime.date(2022, 5, 17), "count": 8},
                {"created_at__date": datetime.date(2022, 5, 18), "count": 7},
                {"created_at__date": datetime.date(2022, 5, 19), "count": 12},
                {"created_at__date": datetime.date(2022, 5, 20), "count": 14},
            ],
            "LA VOZ DE GALICIA": [
                {"created_at__date": datetime.date(2022, 5, 14), "count": 7},
                {"created_at__date": datetime.date(2022, 5, 15), "count": 26},
                {"created_at__date": datetime.date(2022, 5, 16), "count": 13},
                {"created_at__date": datetime.date(2022, 5, 17), "count": 5},
                {"created_at__date": datetime.date(2022, 5, 18), "count": 9},
                {"created_at__date": datetime.date(2022, 5, 19), "count": 6},
                {"created_at__date": datetime.date(2022, 5, 20), "count": 6},
            ],
            "FARO DE VIGO": [
                {"created_at__date": datetime.date(2022, 5, 14), "count": 6},
                {"created_at__date": datetime.date(2022, 5, 15), "count": 7},
                {"created_at__date": datetime.date(2022, 5, 16), "count": 4},
                {"created_at__date": datetime.date(2022, 5, 17), "count": 5},
                {"created_at__date": datetime.date(2022, 5, 18), "count": 2},
                {"created_at__date": datetime.date(2022, 5, 19), "count": 5},
                {"created_at__date": datetime.date(2022, 5, 20), "count": 4},
            ],
        },
        "articles_last_year_by_date_by_source": [
            {"month": datetime.datetime(2021, 7, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 694},
            {"month": datetime.datetime(2021, 8, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 907},
            {"month": datetime.datetime(2021, 9, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 738},
            {"month": datetime.datetime(2021, 10, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 712},
            {"month": datetime.datetime(2021, 11, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 754},
            {"month": datetime.datetime(2021, 12, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 773},
            {"month": datetime.datetime(2022, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 839},
            {"month": datetime.datetime(2022, 2, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 712},
            {"month": datetime.datetime(2022, 3, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 784},
            {"month": datetime.datetime(2022, 4, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")), "total": 738},
        ],
        "article_creation_trend": -0.8805031446540881,
    }
    client = APIClient()
    response = client.get(reverse("articles_metrics"))
    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def load_fake_data():
    with open("tests/integration/api/fake_data.json") as f:
        data = f.read()
        data = json.loads(data)
        articles = []
        for article in data["results"]:
            articles.append(
                Article(
                    title=article["title"],
                    url=article["url"],
                    source=article["source"],
                    image_url=article["image_url"],
                    created_at=article["created_at"],
                )
            )
        Article.objects.bulk_create(articles)


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
            "created_at": article_1.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        {
            "title": article_2.title,
            "url": article_2.url,
            "source": article_2.source,
            "image_url": article_2.image_url,
            "created_at": article_2.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
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


@pytest.mark.xfail(reason="TODO - fix this test")
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
            "created_at": article_1.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    ]
    expected_response = {"count": 1, "next": None, "previous": None, "results": expected_results}
    client = APIClient()
    response = client.get(reverse("articles"), data={"source": Article.FARO_DE_VIGO})
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.xfail(reason="TODO - fix this test")
@pytest.mark.django_db
def test_get_articles_filtered_incorrect_source():
    ArticleFactory(source=Article.FARO_DE_VIGO)
    ArticleFactory(source=Article.MARCA)
    expected_response = {"source": ["Select a valid choice. foo is not one of the available choices."]}
    client = APIClient()
    response = client.get(reverse("articles"), data={"source": "foo"})
    assert response.status_code == 400
    assert response.json() == expected_response
