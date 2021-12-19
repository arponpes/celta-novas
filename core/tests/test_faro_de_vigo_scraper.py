import pytest
from unittest.mock import Mock

from core.scrapers.faro_de_vigo_scraper import execute_fv_scraper
from core.models import Article


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open('core/tests/fixtures/faro_de_vigo.html', 'r') as f:
        mock.content = f.read()
    return mock


@pytest.mark.django_db
def test_execute_fv_scraper(mocker, mock_response):
    mocker.patch('requests.get', return_value=mock_response)
    execute_fv_scraper()
    assert Article.objects.filter(source=Article.FARO_DE_VIGO).exists()
