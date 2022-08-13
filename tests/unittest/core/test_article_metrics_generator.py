from datetime import date

import pytest
from django.utils import timezone

from core.metrics.article_metrics_generator import ArticleMetricsGenerator
from core.models import Article
from tests.unittest.core.factories import ArticleFactory


class TestArticleMetricsGenerator:
    @pytest.mark.django_db
    def test_get_total_articles(self):
        ArticleFactory()
        ArticleFactory()
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_total_articles() == 2

    @pytest.mark.django_db
    def test_get_total_article_zero_articles(self):
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_total_articles() == 0

    @pytest.mark.django_db
    def test_get_articles_last_24_hours(self):
        ArticleFactory(created_at=timezone.now())
        ArticleFactory(created_at=timezone.now())
        ArticleFactory(created_at=date(2020, 1, 1))
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_articles_last_24_hours() == 2

    @pytest.mark.django_db
    def test_get_articles_last_24_hours_zero_articles(self):
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_articles_last_24_hours() == 0

    @pytest.mark.django_db
    def test_get_source_with_more_articles(self):
        ArticleFactory(source=Article.MARCA)
        ArticleFactory(source=Article.MARCA)
        ArticleFactory(source=Article.FARO_DE_VIGO)
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_source_with_more_articles() == {"source": "MARCA", "source__count": 2}

    @pytest.mark.django_db
    def test_get_source_with_more_articles_zero_articles(self):
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_source_with_more_articles() == {"source": "", "source__count": 0}

    @pytest.mark.django_db
    def test_get_source_with_more_articles_last_24_hours(self):
        ArticleFactory(source=Article.MARCA, created_at=timezone.now())
        ArticleFactory(source=Article.MARCA, created_at=timezone.now())
        ArticleFactory(source=Article.FARO_DE_VIGO, created_at=timezone.now())
        ArticleFactory(source=Article.MARCA, created_at=date(2020, 1, 1))
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_source_with_more_articles_last_24_hours() == {
            "source": "MARCA",
            "source__count": 2,
        }

    @pytest.mark.django_db
    def test_get_source_with_more_articles_last_24_hours_zero_articles(self):
        articles = Article.objects.all()
        article_generator = ArticleMetricsGenerator(articles)
        assert article_generator.get_source_with_more_articles_last_24_hours() == {"source": "", "source__count": 0}
