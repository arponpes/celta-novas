import pytest

from core.article_processor.article_processor import ArticleProcessor
from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.crawlers.marca_crawler import MarcaCrawler
from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler
from core.models import Article


@pytest.mark.django_db
def test_execute_moi_celeste_crawler(mocker):
    ap = ArticleProcessor(MoiCelesteCrawler)
    ap.process_articles()
    assert Article.objects.filter(source=Article.MOI_CELESTE).exists()


@pytest.mark.django_db
def test_execute_fv_crawler(mocker):
    ap = ArticleProcessor(FaroDeVigoCrawler)
    ap.process_articles()
    assert Article.objects.filter(source=Article.FARO_DE_VIGO).exists()


@pytest.mark.django_db
def test_execute_marca_crawler(mocker):
    ap = ArticleProcessor(MarcaCrawler)
    ap.process_articles()
    assert Article.objects.filter(source=Article.MARCA).exists()


@pytest.mark.django_db
def test_execute_lv_crawler(mocker):
    ap = ArticleProcessor(LaVozDeGaliciaCrawler)
    ap.process_articles()
    assert Article.objects.filter(source=Article.LA_VOZ_DE_GALICIA).exists()
