from unittest.mock import Mock

import pytest

from core.crawlers.marca_crawler import MarcaCrawler
from core.models import Article


@pytest.fixture
def marca_crawler():
    return MarcaCrawler()


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("core/tests/fixtures/marca.html", "r") as f:
        mock.content = f.read()
    return mock


class TestMarcaCrawler:
    @pytest.mark.django_db
    def test_get_article_url(self, mocker, mock_response, marca_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_url = "https://www.marca.com/futbol/celta/2021/12/25/61c7599ce2704e57938b45eb.html"
        articles = marca_crawler.get_articles()
        assert marca_crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mocker, mock_response, marca_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_title = "El Celta, con la vista en el mercado invernal"
        articles = marca_crawler.get_articles()
        assert marca_crawler.get_article_title(articles[0]).strip() == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mocker, mock_response, marca_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = marca_crawler.get_articles()
        assert len(articles) == 50

    @pytest.mark.django_db
    def test_update_articles(self, mocker, mock_response, marca_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = set(marca_crawler.get_articles())
        assert Article.objects.count() == 0
        marca_crawler.update_articles(articles)
        assert Article.objects.count() == 50

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mocker, mock_response, marca_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = marca_crawler.get_articles()
        assert Article.objects.count() == 0
        marca_crawler.update_articles(articles)
        assert Article.objects.count() == 50
        marca_crawler.update_articles(articles)
        assert Article.objects.count() == 50


@pytest.mark.django_db
def test_execute_marca_crawler(mocker, mock_response, marca_crawler):
    mocker.patch("requests.get", return_value=mock_response)
    marca_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.MARCA).exists()
