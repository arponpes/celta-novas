from core.crawlers.marca_crawler import MarcaCrawler
from core.models import Article
from core.tests.conftest import CommonTest
import pytest


class TestMarcaCrawler(CommonTest):
    crawler = MarcaCrawler()
    fixture = "core/tests/fixtures/marca.html"

    @pytest.mark.django_db
    def test_get_article_url(self, mock_response):
        expected_url = "https://www.marca.com/futbol/celta/2021/12/25/61c7599ce2704e57938b45eb.html"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mock_response):
        expected_title = "El Celta, con la vista en el mercado invernal"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_title(articles[0]).strip() == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mock_response):
        articles = self.crawler.get_articles()
        assert len(articles) == 42

    @pytest.mark.django_db
    def test_update_articles(self, mock_response):
        articles = set(self.crawler.get_articles())
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 42

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mock_response):
        articles = self.crawler.get_articles()
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 42
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 42

    @pytest.mark.django_db
    def test_get_article_image(self, mock_response):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip()
            == "https://phantom-marca.unidadeditorial.es/72c9e239d4d72b736142a8f89848ab95/f/webp/"
            "assets/multimedia/imagenes/2021/12/25/16404543713280_310x174.jpg"
        )

    @pytest.mark.django_db
    def test_execute_marca_crawler(self, mock_response):
        self.crawler.execute_crawler()
        assert Article.objects.filter(source=Article.MARCA).exists()
