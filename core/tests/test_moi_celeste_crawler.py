from unittest.mock import Mock

import pytest

from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler
from core.models import Article


@pytest.fixture
def moi_celeste_crawler():
    return MoiCelesteCrawler()


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("core/tests/fixtures/moi_celeste.html", "r") as f:
        mock.content = f.read()
    return mock


class TestMoiCelesteCrawler:
    @pytest.mark.django_db
    def test_get_article_url(self, mocker, mock_response, moi_celeste_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_url = "http://www.moiceleste.com/2021/12/notas-de-fin-de-ano-15-joseph-aidoo-jr.html"
        articles = moi_celeste_crawler.get_articles()
        assert moi_celeste_crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mocker, mock_response, moi_celeste_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        expected_title = "Notas de fin de año | #15 Joseph Aidoo Jr."
        articles = moi_celeste_crawler.get_articles()
        assert moi_celeste_crawler.get_article_title(articles[0]).strip() == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mocker, mock_response, moi_celeste_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = moi_celeste_crawler.get_articles()
        assert len(articles) == 25

    @pytest.mark.django_db
    def test_update_articles(self, mocker, mock_response, moi_celeste_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = set(moi_celeste_crawler.get_articles())
        assert Article.objects.count() == 0
        moi_celeste_crawler.update_articles(articles)
        assert Article.objects.count() == 25

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mocker, mock_response, moi_celeste_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = moi_celeste_crawler.get_articles()
        assert Article.objects.count() == 0
        moi_celeste_crawler.update_articles(articles)
        assert Article.objects.count() == 25
        moi_celeste_crawler.update_articles(articles)
        assert Article.objects.count() == 25

    @pytest.mark.django_db
    def test_get_article_image(self, mocker, mock_response, moi_celeste_crawler):
        mocker.patch("requests.get", return_value=mock_response)
        articles = moi_celeste_crawler.get_articles()
        assert (
            moi_celeste_crawler.get_article_img(articles[0])
            == "https://blogger.googleusercontent.com/img/a/AVvXsEhp_nsWJlxVew6KY0SxDtALsQikzdHh76or3mRKAOgPJt68Gs3c"
            "WxAbL6lq9IaEhyLn_tQ8wQGlRngccj0mdXMvEtDCpujfsRNCyqUOuuUsHPhmfN2s4krY14O0rNXd7W5X_RSHXFm98D5HO"
            "cYgL-U9rMZDoE74gmn_WRYqqYHgqC3mVeI_FfVOj9Pl6A=w640-h442"
        )


@pytest.mark.django_db
def test_execute_moi_celeste_crawler(mocker, mock_response, moi_celeste_crawler):
    mocker.patch("requests.get", return_value=mock_response)
    moi_celeste_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.MOI_CELESTE).exists()
