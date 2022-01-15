import os

import requests
from celery import shared_task

from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.crawlers.la_voz_de_galicia_crawler import LaVozDeGaliciaCrawler
from core.crawlers.marca_crawler import MarcaCrawler
from core.crawlers.moi_celeste_crawler import MoiCelesteCrawler
from core.helpers.check_article_status import check_article_status


@shared_task
def task_fv_scraper():
    faro_de_vigo_crawler = FaroDeVigoCrawler()
    faro_de_vigo_crawler.execute_crawler()
    requests.get(f'https://hc-ping.com/{os.environ.get("fv_hc_ping")}', timeout=10)


@shared_task
def task_lv_scraper():
    la_voz_de_galicia_crawler = LaVozDeGaliciaCrawler()
    la_voz_de_galicia_crawler.execute_crawler()
    requests.get(f'https://hc-ping.com/{os.environ.get("lv_hc_ping")}', timeout=10)


@shared_task
def task_marca_scraper():
    marca_crawler = MarcaCrawler()
    marca_crawler.execute_crawler()
    requests.get(f'https://hc-ping.com/{os.environ.get("marca_hc_ping")}', timeout=10)


@shared_task
def task_mc_scraper():
    moi_celeste_crawler = MoiCelesteCrawler()
    moi_celeste_crawler.execute_crawler()
    requests.get(f'https://hc-ping.com/{os.environ.get("mc_hc_ping")}', timeout=10)


@shared_task
def task_check_article_status():
    if check_article_status():
        requests.get(f'https://hc-ping.com/{os.environ.get("article_status_hc_ping")}', timeout=10)
