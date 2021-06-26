import requests
from bs4 import BeautifulSoup
from core.models import Article


SOURCE = Article.MOI_CELESTE
URL = 'http://www.moiceleste.com/'


def _get_articles() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('h3', class_='post-title')


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


def execute_mc_scraper():
    articles = _get_articles()
    _update_articles(articles)
