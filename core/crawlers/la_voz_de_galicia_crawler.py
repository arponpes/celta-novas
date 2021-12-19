from core.models import Article
from .utils import get_soup
from .common import CrawlerBase


class LaVozDeGaliciaCrawler(CrawlerBase):
    source = Article.LA_VOZ_DE_GALICIA
    url_base = "https://www.lavozdegalicia.es/"
    url = f"{url_base}gradario/"

    def get_article_url(self, article) -> str:
        return f'{self.url_base}{article.find("a")["href"]}'

    def get_article_title(self, article) -> str:
        return article.find('a').text.strip()

    def get_articles(self) -> list:
        soup = get_soup(self.url)
        return soup.find_all("h2", itemprop="headline")
