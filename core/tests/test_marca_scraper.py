import pytest

from core.scrapers.marca_scraper import execute_marca_scraper
from core.models import Article


@pytest.mark.django_db
def test_execute_marca_scraper():
    execute_marca_scraper()
    assert Article.objects.filter(source=Article.MARCA).exists()
