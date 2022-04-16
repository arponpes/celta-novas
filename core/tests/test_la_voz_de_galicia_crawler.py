from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.models import Article
from core.tests.conftest import CommonTest
import pytest


class TestLaVozDeGaliciaCrawler(CommonTest):
    crawler = LaVozDeGaliciaCrawler()
    fixture = "core/tests/fixtures/la_voz_de_galicia.html"

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
    def test_update_articles(self, mock_response):
        articles = set(self.crawler.get_articles())
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 48

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mock_response):
        articles = self.crawler.get_articles()
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 48
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 48

    @pytest.mark.django_db
    def test_get_article_image(self, mock_response):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip()
            == "https://cflvdg.avoz.es/sc/ZYbdY4WqJmCau-YBzXVRgZUigak=/450x/2021/12/24/"
            "00121640366288246778661/Foto/54353454543534.JPG"
        )

    @pytest.mark.django_db
    def test_execute_lv_crawler(self, mock_response):
        self.crawler.execute_crawler()
        assert Article.objects.filter(source=Article.LA_VOZ_DE_GALICIA).exists()
