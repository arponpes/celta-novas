import pytest
from unittest.mock import Mock

from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler
from core.models import Article


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("core/tests/fixtures/moi_celeste.html", "r") as f:
        mock.content = f.read()
    return mock


@pytest.mark.django_db
def test_execute_mc_crawler(mocker, mock_response):
    mocker.patch("requests.get", return_value=mock_response)
    moi_celete_crawler = MoiCelesteCrawler()
    moi_celete_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.MOI_CELESTE).exists()
