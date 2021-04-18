import requests
from bs4 import BeautifulSoup
from ..core.models import New


SOURCE = 'VG'
URL_PREFIX = 'https://www.lavozdegalicia.es/'
URL = f'{URL_PREFIX}gradario/'


def _get_news() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('h2', itemprop='headline')


def update_news(news):
    for new in news:
        url = f'{URL_PREFIX}{new.find("a")["href"]}'
        title = new.find('a').text.strip()
        if New.objects.filter(url=url).exists():
            continue
        New(
            title=title,
            url=url,
            source=SOURCE
        ).save()


if __name__ == '__main__':
    update_news()
