import pytest
from unittest.mock import Mock

from core.crawlers.marca_crawler import MarcaCrawler
from core.models import Article


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.status_code = 200
    with open('core/tests/fixtures/marca.html', 'r') as f:
        mock.content = f.read()
    return mock


@pytest.mark.django_db
def test_execute_marca_crawler(mocker, mock_response):
    mocker.patch('requests.get', return_value=mock_response)
    marca_crawler = MarcaCrawler()
    marca_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.MARCA).exists()
