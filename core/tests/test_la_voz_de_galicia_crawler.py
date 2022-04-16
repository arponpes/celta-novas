from unittest.mock import Mock

from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.models import Article
import pytest


@pytest.fixture
def la_voz_de_galicia_crawler():
    return LaVozDeGaliciaCrawler()


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("core/tests/fixtures/la_voz_de_galicia.html", "r") as f:
        mock.content = f.read()
    return mock


class TestLaVozDeGaliciaCrawler:
    @pytest.mark.django_db
    def test_get_article_url(self, mocker, mock_response, la_voz_de_galicia_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_url = (
            "https://www.lavozdegalicia.es//noticia/gradario/2021/12/24/"
            "felicitaciones-celtistas/00031640337006491729817.htm"
        )
        articles = la_voz_de_galicia_crawler.get_articles()
        assert la_voz_de_galicia_crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mocker, mock_response, la_voz_de_galicia_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_title = "Así felicitan la Navidad jugadores y afición del Celta"
        articles = la_voz_de_galicia_crawler.get_articles()
        assert la_voz_de_galicia_crawler.get_article_title(articles[0]) == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mocker, mock_response, la_voz_de_galicia_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = la_voz_de_galicia_crawler.get_articles()
        assert len(articles) == 50

    @pytest.mark.django_db
    def test_update_articles(self, mocker, mock_response, la_voz_de_galicia_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = set(la_voz_de_galicia_crawler.get_articles())
        assert Article.objects.count() == 0
        la_voz_de_galicia_crawler.update_articles(articles)
        assert Article.objects.count() == 48

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mocker, mock_response, la_voz_de_galicia_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = la_voz_de_galicia_crawler.get_articles()
        assert Article.objects.count() == 0
        la_voz_de_galicia_crawler.update_articles(articles)
        assert Article.objects.count() == 48
        la_voz_de_galicia_crawler.update_articles(articles)
        assert Article.objects.count() == 48

    @pytest.mark.django_db
    def test_get_article_image(self, mocker, mock_response, la_voz_de_galicia_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = la_voz_de_galicia_crawler.get_articles()
        assert (
            la_voz_de_galicia_crawler.get_article_img(articles[0]).strip()
            == "https://cflvdg.avoz.es/sc/ZYbdY4WqJmCau-YBzXVRgZUigak=/450x/2021/12/24/"
            "00121640366288246778661/Foto/54353454543534.JPG"
        )


@pytest.mark.django_db
def test_execute_lv_crawler(mocker, mock_response):
    mocker.patch("requests.get", return_value=mock_response)
    la_voz_de_galicia_crawler = LaVozDeGaliciaCrawler()
    la_voz_de_galicia_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.LA_VOZ_DE_GALICIA).exists()
