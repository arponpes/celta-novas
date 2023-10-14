import pytest

from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.models import Article
from tests.unittest.conftest import CommonTest


class TestLaVozDeGaliciaCrawler(CommonTest):
    crawler = LaVozDeGaliciaCrawler()
    fixture = "tests/unittest/core/fixtures/la_voz_de_galicia.html"

    @pytest.mark.django_db
    def test_get_article_url(self):
        expected_url = (
            "https://www.lavozdegalicia.es//noticia/gradario/2023/09/23/"
            "celta-echa-borda-siete-minutos-3-2/00031695494384727759350.htm"
        )
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self):
        expected_title = "El Celta echa todo por la borda en siete minutos (3-2)"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_title(articles[0]) == expected_title

    @pytest.mark.django_db
    def test_get_articles(self):
        articles = self.crawler.get_articles()
        assert len(articles) == 53

    @pytest.mark.django_db
    def test_get_article_image(self):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip()
            == "https://cflvdg.avoz.es/sc/b2u0IF8evhTwQVSWWpsFcfhbQ9M=/768x/2023/09/23"
            "/00121695494221437515672/Foto/reu_20230923_182936612.jpg"
        )

    @pytest.mark.django_db
    def test_execute_crawler(self):
        articles = self.crawler.execute_crawler()
        assert len(articles) == 49
        for article in articles:
            assert article.source == Article.LA_VOZ_DE_GALICIA
            assert article.url
            assert article.title
