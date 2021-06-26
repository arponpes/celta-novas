import requests
from bs4 import BeautifulSoup
from core.models import Article


SOURCE = Article.FARO_DE_VIGO
URL_PREFIX = 'https://galego.farodevigo.es/'
URL = f'{URL_PREFIX}celta-de-vigo/'


def _get_articles() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('a', class_='new__headline')


def _update_articles(articles):
    for article in articles:
        url = f'{URL_PREFIX}{article["href"]}'
        title = article.text.strip()
        if Article.objects.filter(url=url).exists():
            continue
        Article(
            title=title,
            url=url,
            source=SOURCE
        ).save()


def execute_fv_scraper():
    articles = _get_articles()
    _update_articles(articles)
