from datetime import timedelta

import pytest
from django.utils import timezone

from core.helpers.healthcheck import check_article_status
from core.models import Article
from tests.unittest.core.factories import ArticleFactory


@pytest.mark.django_db
def test_check_article_status():
    for source in Article.SOURCE_CHOICES:
        ArticleFactory(source=source[0], created_at=timezone.now())
    assert check_article_status()


@pytest.mark.django_db
def test_check_article_status_no_articles():
    for source in Article.SOURCE_CHOICES:
        ArticleFactory(source=source[0], created_at=timezone.now() - timedelta(hours=48))
    assert not check_article_status()
