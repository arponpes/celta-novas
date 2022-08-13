from unittest.mock import Mock

import pytest
from bs4 import BeautifulSoup

from core.crawlers.common import CrawlerBase
from tests.unittest.core.factories import ArticleFactory


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("tests/unittest/core/fixtures/faro_de_vigo.html", "r") as f:
        mock.content = f.read()
    return mock


@pytest.fixture
def mock_response_error():
    mock = Mock()
    mock.status_code = 404
    return mock


class TestCrawlerBase:
    @pytest.mark.django_db
    def test_normalize_url(self):
        assert CrawlerBase.normalize_url(CrawlerBase(), "www.foo.com/foo") == "https://www.foo.com/foo"

    @pytest.mark.django_db
    def test_get_soup(self, mocker, mock_response):
        mocker.patch("requests.get", return_value=mock_response)
        assert isinstance(CrawlerBase.get_soup(CrawlerBase(), "foo"), BeautifulSoup)

    @pytest.mark.django_db
    def test_make_request(self, mocker, mock_response):
        mocker.patch("requests.get", return_value=mock_response)
        assert CrawlerBase.make_requests(CrawlerBase(), "foo") == mock_response.content

    @pytest.mark.django_db
    def test_make_request_error(self, mocker, mock_response_error):
        mocker.patch("requests.get", return_value=mock_response_error)
        assert CrawlerBase.make_requests(CrawlerBase(), "foo") == ""
