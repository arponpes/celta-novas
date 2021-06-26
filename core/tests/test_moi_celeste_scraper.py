import pytest

from core.scrapers.moi_celeste_scraper import execute_mc_scraper
from core.models import Article


@pytest.mark.django_db
def test_execute_mc_scraper():
    execute_mc_scraper()
    assert Article.objects.filter(source=Article.MOI_CELESTE).exists()
