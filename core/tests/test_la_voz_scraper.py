import pytest

from core.scrapers.la_voz_scraper import execute_lv_scraper
from core.models import Article


@pytest.mark.django_db
def test_execute_lv_scraper():
    execute_lv_scraper()
    assert Article.objects.filter(source=Article.LA_VOZ_DE_GALICIA).exists()
