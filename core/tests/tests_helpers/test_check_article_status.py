import pytest

from core.tests.factories import ArticleFactory
from core.helpers.check_article_status import check_article_status
from core.models import Article
from datetime import date


@pytest.mark.django_db
def test_check_article_status():
    for source in Article.SOURCE_CHOICES:
        ArticleFactory(source=source[0])
    assert check_article_status()


@pytest.mark.django_db
def test_check_article_status_no_articles():
    for source in Article.SOURCE_CHOICES:
        old_article = ArticleFactory(
            source=source[0], created_at=date(2000, 1, 1)
        )
        old_article.created_at = date(2020, 1, 1)
        old_article.save()
    assert not check_article_status()
