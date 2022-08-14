import pytest

from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.models import Article
from tests.unittest.conftest import CommonTest


class TestLaVozDeGaliciaCrawler(CommonTest):
    crawler = LaVozDeGaliciaCrawler()
    fixture = "tests/unittest/core/fixtures/la_voz_de_galicia.html"

    @pytest.mark.django_db
    def test_get_article_url(self, mock_response):
        expected_url = (
            "https://www.lavozdegalicia.es//noticia/gradario/2021/12/24/"
            "felicitaciones-celtistas/00031640337006491729817.htm"
        )
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mock_response):
        expected_title = "Así felicitan la Navidad jugadores y afición del Celta"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_title(articles[0]) == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mock_response):
        articles = self.crawler.get_articles()
        assert len(articles) == 50

    @pytest.mark.django_db
    def test_get_article_image(self, mock_response):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip()
            == "https://cflvdg.avoz.es/sc/ZYbdY4WqJmCau-YBzXVRgZUigak=/450x/2021/12/24/"
            "00121640366288246778661/Foto/54353454543534.JPG"
        )

    @pytest.mark.django_db
    def test_execute_crawler(self, mock_response):
        articles = self.crawler.execute_crawler()
        assert len(articles) == 42
        for article in articles:
            assert article.source == Article.LA_VOZ_DE_GALICIA
            assert article.url
            assert article.title
