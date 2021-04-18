import requests
from bs4 import BeautifulSoup
from ..models import New


SOURCE = 'FV'
URL_PREFIX = 'https://galego.farodevigo.es/'
URL = f'{URL_PREFIX}celta-de-vigo/'


def _get_news() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('a', class_='new__headline')


def update_news(news):
    for new in news:
        url = f'{URL_PREFIX}{new["href"]}'
        title = new.text.strip()
        if New.objects.filter(url=url).exists():
            continue
        New(
            title=title,
            url=url,
            source=SOURCE
        ).save()
