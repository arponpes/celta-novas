from core.models import Article
from .utils import to_be_created, get_soup


SOURCE = Article.LA_VOZ_DE_GALICIA
URL_PREFIX = 'https://www.lavozdegalicia.es/'
URL = f'{URL_PREFIX}gradario/'


def get_articles() -> list:
    soup = get_soup(URL)
    return soup.find_all('h2', itemprop='headline')


def update_articles(articles):
    for article in articles:
        url = f'{URL_PREFIX}{article.find("a")["href"]}'
        title = article.find('a').text.strip()
        if not to_be_created(title, url):
            continue
        Article(title=title, url=url, source=SOURCE).save()


def execute_lv_scraper():
    articles = get_articles()
    update_articles(articles)
