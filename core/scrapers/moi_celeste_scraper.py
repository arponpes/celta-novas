import requests
from bs4 import BeautifulSoup
from ..core.models import New


SOURCE = 'MC'
URL = 'http://www.moiceleste.com/'


def _get_news() -> list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('h3', class_='post-title')


def update_news(news):
    for new in news:
        url = new.find('a')['href']
        if New.objects.filter(url=url).exists():
            continue
        New(
            title=new.find('a').text,
            url=url,
            source=SOURCE
        ).save()


if __name__ == '__main__':
    update_news()
