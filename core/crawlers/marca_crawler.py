from core.models import Article

from .common import CrawlerBase


class MarcaCrawler(CrawlerBase):
    source = Article.MARCA
    url = "https://www.marca.com/futbol/celta.html"

    def get_article_url(self, article):
        return article.find("h3").find("a")["href"]

    def get_article_title(self, article):
        return article.find("h3").find("a").text

    def get_article_img(self, article):
        return article.find("picture").find("source")["srcset"].strip()

    def get_articles(self) -> list:
        soup = self.get_soup(self.url)
        return soup.find_all("article", class_="mod-item mod-futbol")
