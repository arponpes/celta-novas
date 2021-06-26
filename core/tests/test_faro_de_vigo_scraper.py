import pytest

from core.scrapers.faro_de_vigo_scraper import execute_fv_scraper
from core.models import Article


@pytest.mark.django_db
def test_execute_fv_scraper():
    execute_fv_scraper()
    assert Article.objects.filter(source=Article.FARO_DE_VIGO).exists()
