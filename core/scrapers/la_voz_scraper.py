import requests
from bs4 import BeautifulSoup
from core.models import Article


SOURCE = Article.LA_VOZ_DE_GALICIA
URL_PREFIX = 'https://www.lavozdegalicia.es/'
URL = f'{URL_PREFIX}gradario/'


def _get_articles() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('h2', itemprop='headline')


def _update_articles(articles):
    for article in articles:
        url = f'{URL_PREFIX}{article.find("a")["href"]}'
        title = article.find('a').text.strip()
        if Article.objects.filter(url=url).exists():
            continue
        Article(
            title=title,
            url=url,
            source=SOURCE
        ).save()


def execute_lv_scraper():
    articles = _get_articles()
    _update_articles(articles)
