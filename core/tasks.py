from celery import shared_task

from core.article_processor.article_processor import ArticleProcessor
from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.crawlers.marca_crawler import MarcaCrawler
from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler


@shared_task
def task_fv_scraper():
    ap = ArticleProcessor(FaroDeVigoCrawler)
    ap.process_articles()


@shared_task
def task_lv_scraper():
    ap = ArticleProcessor(LaVozDeGaliciaCrawler)
    ap.process_articles()


@shared_task
def task_marca_scraper():
    ap = ArticleProcessor(MarcaCrawler)
    ap.process_articles()


@shared_task
def task_mc_scraper():
    ap = ArticleProcessor(MoiCelesteCrawler)
    ap.process_articles()
