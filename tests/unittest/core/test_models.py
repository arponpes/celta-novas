import pytest

from core.models import Article
from tests.unittest.core.factories import ArticleFactory


@pytest.mark.django_db
def test_new_test_creation():
    article_test = ArticleFactory()
    assert isinstance(article_test, Article)
