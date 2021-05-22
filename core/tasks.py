from celery import shared_task
from core.scrapers.faro_de_vigo_scraper import execute_fv_scraper
from core.scrapers.la_voz_scraper import execute_lv_scraper
from core.scrapers.marca_scraper import execute_marca_scraper
from core.scrapers.moi_celeste_scraper import execute_mc_scraper


@shared_task
def task_fv_scraper():
    execute_fv_scraper()


@shared_task
def task_lv_scraper():
    execute_lv_scraper()


@shared_task
def task_marca_scraper():
    execute_marca_scraper()


@shared_task
def task_mc_scraper():
    execute_mc_scraper()
