from core.crawlers.marca_crawler import MarcaCrawler
from core.models import Article
from tests.unittest.conftest import CommonTest
import pytest


class TestMarcaCrawler(CommonTest):
    crawler = MarcaCrawler()
    fixture = "tests/unittest/core/fixtures/marca.html"

    @pytest.mark.django_db
    def test_get_article_url(self, mock_response):
        expected_url = "https://www.marca.com/futbol/primera-division/2022/06/24/62b58ab4e2704ec4958b45ab.html"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mock_response):
        expected_title = "Calendario de partidos de pretemporada de los equipos de Primera división"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_title(articles[0]).strip() == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mock_response):
        articles = self.crawler.get_articles()
        assert len(articles) == 50

    @pytest.mark.django_db
    def test_update_articles(self, mock_response):
        articles = set(self.crawler.get_articles())
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 50

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mock_response):
        articles = self.crawler.get_articles()
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 50
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 50

    @pytest.mark.django_db
    def test_get_article_image(self, mock_response):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip()
            == "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2022/06/24/16560701441413.jpg"
        )
