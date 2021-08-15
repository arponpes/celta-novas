from core.models import Article
from .utils import to_be_created, get_soup


SOURCE = Article.FARO_DE_VIGO
URL_PREFIX = 'https://galego.farodevigo.es/'
URL = f'{URL_PREFIX}celta-de-vigo/'


def get_articles() -> list:
    soup = get_soup(URL)
    return soup.find_all('a', class_='new__headline')


def update_articles(articles):
    for article in articles:
        url = f'{URL_PREFIX}{article["href"]}'
        title = article.text.strip()
        if not to_be_created(title, url):
            continue

        Article(title=title, url=url, source=SOURCE).save()


def execute_fv_scraper():
    articles = get_articles()
    update_articles(articles)
