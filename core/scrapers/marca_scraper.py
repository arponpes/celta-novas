import requests
from bs4 import BeautifulSoup
from core.models import Article


SOURCE = Article.MARCA
URL = 'https://www.marca.com/futbol/celta.html'


def _get_articles() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('h3', class_='mod-title')


def _update_articles(articles):
    for article in articles:
        url = article.find('a')['href']
        if Article.objects.filter(url=url).exists():
            continue
        Article(
            title=article.find('a').text,
            url=url,
            source=SOURCE
        ).save()


def execute_marca_scraper():
    articles = _get_articles()
    _update_articles(articles)
