import os

import requests
from celery import shared_task

from core.article_processor.article_processor import ArticleProcessor
from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.crawlers.marca_crawler import MarcaCrawler
from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler
from core.helpers.healthcheck import check_article_status


@shared_task
def task_fv_scraper():
    ap = ArticleProcessor(FaroDeVigoCrawler)
    ap.process_articles()
    requests.get(f'https://hc-ping.com/{os.environ.get("fv_hc_ping")}', timeout=10)


@shared_task
def task_lv_scraper():
    ap = ArticleProcessor(LaVozDeGaliciaCrawler)
    ap.process_articles()
    requests.get(f'https://hc-ping.com/{os.environ.get("lv_hc_ping")}', timeout=10)


@shared_task
def task_marca_scraper():
    ap = ArticleProcessor(MarcaCrawler)
    ap.process_articles()
    requests.get(f'https://hc-ping.com/{os.environ.get("marca_hc_ping")}', timeout=10)


@shared_task
def task_mc_scraper():
    ap = ArticleProcessor(MoiCelesteCrawler)
    ap.process_articles()
    requests.get(f'https://hc-ping.com/{os.environ.get("mc_hc_ping")}', timeout=10)


@shared_task
def task_check_article_status():
    if check_article_status():
        requests.get(f'https://hc-ping.com/{os.environ.get("article_status_hc_ping")}', timeout=10)
