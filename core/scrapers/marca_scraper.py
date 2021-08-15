from core.models import Article
from .utils import to_be_created, get_soup


SOURCE = Article.MARCA
URL = 'https://www.marca.com/futbol/celta.html'


def get_articles() -> list:
    soup = get_soup(URL)
    return soup.find_all('h3', class_='mod-title')


def update_articles(articles):
    for article in articles:
        url = article.find('a')['href']
        title = article.find('a').text
        if not to_be_created(title, url):
            continue

        Article(title=title, url=url, source=SOURCE).save()


def execute_marca_scraper():
    articles = get_articles()
    update_articles(articles)
