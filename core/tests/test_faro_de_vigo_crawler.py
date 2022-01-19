from unittest.mock import Mock

import pytest

from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.models import Article


@pytest.fixture
def faro_de_vigo_crawler():
    return FaroDeVigoCrawler()


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("core/tests/fixtures/faro_de_vigo.html", "r") as f:
        mock.content = f.read()
    return mock


class TestFaroDeVigoCrawler:
    @pytest.mark.django_db
    def test_get_article_url(self, mocker, mock_response, faro_de_vigo_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_url = (
            "https://galego.farodevigo.es//celta-de-vigo/2022/01/19/celta-logra-triunfo-madurez-frente-61747882.html"
        )
        articles = faro_de_vigo_crawler.get_articles()
        assert faro_de_vigo_crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mocker, mock_response, faro_de_vigo_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_title = "El Celta firma un triunfo de madurez"
        articles = faro_de_vigo_crawler.get_articles()
        assert faro_de_vigo_crawler.get_article_title(articles[0]) == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mocker, mock_response, faro_de_vigo_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = faro_de_vigo_crawler.get_articles()
        assert len(articles) == 17

    @pytest.mark.django_db
    def test_update_articles(self, mocker, mock_response, faro_de_vigo_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = set(faro_de_vigo_crawler.get_articles())
        assert Article.objects.count() == 0
        faro_de_vigo_crawler.update_articles(articles)
        assert Article.objects.count() == 17

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mocker, mock_response, faro_de_vigo_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = faro_de_vigo_crawler.get_articles()
        assert Article.objects.count() == 0
        faro_de_vigo_crawler.update_articles(articles)
        assert Article.objects.count() == 17
        faro_de_vigo_crawler.update_articles(articles)
        assert Article.objects.count() == 17

    @pytest.mark.django_db
    def test_get_article_image(self, mocker, mock_response, faro_de_vigo_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = faro_de_vigo_crawler.get_articles()
        assert (
            faro_de_vigo_crawler.get_article_img(articles[0]).strip() == "https://estaticos-cdn.prensaiberica.es/clip/"
            "eee3962b-a83e-4d3f-8da3-5c838d59f61c_21-9-aspect-ratio_default_0_x2278y1104.jpg"
        )


@pytest.mark.django_db
def test_execute_fv_crawler(mocker, mock_response, faro_de_vigo_crawler):
    mocker.patch("requests.get", return_value=mock_response)
    faro_de_vigo_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.FARO_DE_VIGO).exists()
