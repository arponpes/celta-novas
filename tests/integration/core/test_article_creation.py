from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.crawlers.marca_crawler import MarcaCrawler
from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler
from core.models import Article
import pytest


@pytest.mark.django_db
def test_execute_moi_celeste_crawler():
    moi_celeste_crawler = MoiCelesteCrawler()
    moi_celeste_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.MOI_CELESTE).exists()


@pytest.mark.django_db
def test_execute_fv_crawler():
    faro_de_vigo_crawler = FaroDeVigoCrawler()
    faro_de_vigo_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.FARO_DE_VIGO).exists()


@pytest.mark.django_db
def test_execute_marca_crawler():
    marca_crawler = MarcaCrawler()
    marca_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.MARCA).exists()


@pytest.mark.django_db
def test_execute_lv_crawler():
    la_voz_de_galicia_crawler = LaVozDeGaliciaCrawler()
    la_voz_de_galicia_crawler.execute_crawler()
    assert Article.objects.filter(source=Article.LA_VOZ_DE_GALICIA).exists()
