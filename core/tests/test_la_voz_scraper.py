import pytest
from unittest.mock import Mock

from core.scrapers.la_voz_scraper import LaVozDeGaliciaCrawler
from core.models import Article


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open("core/tests/fixtures/la_voz_de_galicia.html", "r") as f:
        mock.content = f.read()
    return mock


@pytest.mark.django_db
def test_execute_lv_scraper(mocker, mock_response):
    mocker.patch("requests.get", return_value=mock_response)
    la_voz_de_galicia_crawler = LaVozDeGaliciaCrawler()
    la_voz_de_galicia_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.LA_VOZ_DE_GALICIA).exists()
