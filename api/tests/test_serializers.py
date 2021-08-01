import pytest
import datetime
from core.models import Article
from api.serializers import ArticleSerializer
from rest_framework.exceptions import ValidationError


@pytest.mark.django_db
def test_article_serializer():
    expected_results = {
        'title': 'foo',
        'url': 'https://www.foo.com/article',
        'source': Article.MARCA,
        'created_at': str(datetime.datetime.now()),
    }

    article = Article(**expected_results)

    results = ArticleSerializer(article).data

    assert results == expected_results


def test_raise_error_when_missing_required_field():
    incomplete_data = {
        'title': 'foo',
        'source': Article.MARCA,
        'created_at': str(datetime.datetime.now()),
    }

    serializer = ArticleSerializer(data=incomplete_data)

    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
