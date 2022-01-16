from core.models import Article

from .common import CrawlerBase
from .mixings import CrawlerMixin


class MoiCelesteCrawler(CrawlerBase, CrawlerMixin):
    source = Article.MOI_CELESTE
    url = "http://www.moiceleste.com/"

    def get_article_url(self, article):
        return article.find("h3").find("a")["href"]

    def get_article_title(self, article):
        return article.find("h3").find("a").text

    def get_article_img(self, article):
        return article.find("div", class_="post-body").find("img")["src"]

    def get_articles(self) -> list:
        soup = self.get_soup(self.url)
        return soup.find_all("div", class_="post hentry")
