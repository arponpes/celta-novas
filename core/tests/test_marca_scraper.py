import pytest
from unittest.mock import Mock

from core.scrapers.marca_scraper import execute_marca_scraper
from core.models import Article


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open('core/tests/html_mocks/marca.html', 'r') as f:
        mock.content = f.read()
    return mock


@pytest.mark.django_db
def test_execute_marca_scraper(mocker, mock_response):
    mocker.patch('requests.get', return_value=mock_response)
    execute_marca_scraper()
    assert Article.objects.filter(source=Article.MARCA).exists()
