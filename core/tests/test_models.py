from core.models import Article
import pytest

from .factories import ArticleFactory


@pytest.mark.django_db
def test_new_test_creation():
    article_test = ArticleFactory()
    assert isinstance(article_test, Article)
