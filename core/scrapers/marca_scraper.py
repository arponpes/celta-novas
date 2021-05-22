import requests
from bs4 import BeautifulSoup
from core.models import New


SOURCE = 'MR'
URL = 'https://www.marca.com/futbol/celta.html'


def _get_news() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('h3', class_='mod-title')


def _update_news(news):
    for new in news:
        url = new.find('a')['href']
        if New.objects.filter(url=url).exists():
            continue
        New(
            title=new.find('a').text,
            url=url,
            source=SOURCE
        ).save()


def execute_marca_scraper():
    news = _get_news()
    _update_news(news)
