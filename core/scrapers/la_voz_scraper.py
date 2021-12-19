from core.models import Article
from .utils import get_soup
from .common import CrawlerBase


class LaVozDeGaliciaCrawler(CrawlerBase):
    source = Article.LA_VOZ_DE_GALICIA
    url_base = "https://www.lavozdegalicia.es/"
    url = f"{url_base}gradario/"

    def get_articles(self) -> list:
        soup = get_soup(self.url)
        return soup.find_all("h2", itemprop="headline")
