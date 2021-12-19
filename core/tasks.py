import os
import requests
from celery import shared_task
from core.scrapers.faro_de_vigo_scraper import FaroDeVigoCrawler
from core.scrapers.la_voz_scraper import execute_lv_scraper
from core.scrapers.marca_scraper import execute_marca_scraper
from core.scrapers.moi_celeste_scraper import execute_mc_scraper
from core.helpers.check_article_status import check_article_status


@shared_task
def task_fv_scraper():
    faro_de_vigo_crawler = FaroDeVigoCrawler()
    faro_de_vigo_crawler.execute_crawler()
    requests.get(
        f'https://hc-ping.com/{os.environ.get("fv_hc_ping")}', timeout=10
    )


@shared_task
def task_lv_scraper():
    execute_lv_scraper()
    requests.get(
        f'https://hc-ping.com/{os.environ.get("lv_hc_ping")}', timeout=10
    )


@shared_task
def task_marca_scraper():
    execute_marca_scraper()
    requests.get(
        f'https://hc-ping.com/{os.environ.get("marca_hc_ping")}', timeout=10
    )


@shared_task
def task_mc_scraper():
    execute_mc_scraper()
    requests.get(
        f'https://hc-ping.com/{os.environ.get("mc_hc_ping")}', timeout=10
    )


@shared_task
def task_check_article_status():
    if check_article_status():
        requests.get(
            f'https://hc-ping.com/{os.environ.get("article_status_hc_ping")}',
            timeout=10
        )
