import pytest

from core.article_processor.article_processor import ArticleProcessor
from core.crawlers.marca_crawler import MarcaCrawler
from core.models import Article
from tests.unittest.core.factories import ArticleFactory


class TestArticleProcessor:
    article_processor_class = ArticleProcessor(crawler_class=MarcaCrawler)

    @pytest.mark.django_db
    def test_update_articles(self, mocker):
        article_duplicated = ArticleFactory()
        self.article_processor_class.save_article(article_duplicated)
        articles = [
            ArticleFactory(title="foo", url="http://foo.com"),
            ArticleFactory(title="bar", url="http://bar.com"),
            ArticleFactory(title="hoge", url="http://hoge.com"),
            article_duplicated,
        ]
        self.article_processor_class.update_articles(articles)
        assert Article.objects.count() == 4

    @pytest.mark.django_db
    def test_save_article(self):
        article = ArticleFactory()
        self.article_processor_class.save_article(article)
        assert Article.objects.filter(title=article.title).exists()

    @pytest.mark.django_db
    def test_to_be_created_true(self):
        assert self.article_processor_class.to_be_created("foo", "http://foo.com")

    @pytest.mark.django_db
    def test_to_be_created_false(self):
        ArticleFactory(title="foo", url="http://foo.com")
        assert not self.article_processor_class.to_be_created("foo", "http://foo.com")
