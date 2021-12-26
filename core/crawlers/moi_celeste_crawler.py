from core.models import Article

from .common import CrawlerBase
from .utils import get_soup


class MoiCelesteCrawler(CrawlerBase):
    source = Article.MOI_CELESTE
    url = "http://www.moiceleste.com/"

    def get_article_url(self, article):
        return article.find("a")["href"]

    def get_article_title(self, article):
        return article.find("a").text

    def get_articles(self) -> list:
        soup = get_soup(self.url)
        return soup.find_all("h3", class_="post-title")
