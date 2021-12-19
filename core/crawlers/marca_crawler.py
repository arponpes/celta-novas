from core.models import Article
from .utils import get_soup
from .common import CrawlerBase


class MarcaCrawler(CrawlerBase):
    source = Article.MARCA
    url = "https://www.marca.com/futbol/celta.html"

    def get_article_url(self, article):
        return article.find('a')['href']

    def get_article_title(self, article):
        return article.find('a').text

    def get_articles(self) -> list:
        soup = get_soup(self.url)
        return soup.find_all('h3', class_='mod-title')
