import re
import urllib.parse

from core.models import Article

from .common import CrawlerBase


class LaVozDeGaliciaCrawler(CrawlerBase):
    source = Article.LA_VOZ_DE_GALICIA
    url_base = "https://www.lavozdegalicia.es/"
    url = urllib.parse.urljoin(url_base, "gradario/")

    def get_article_url(self, article) -> str:
        url = f'{self.url_base}{article.find("h4").find("a")["href"]}'
        if re.findall(r"video/gradario", url):
            return ""
        return url

    def get_article_title(self, article) -> str:
        return article.find("h4").find("a").text.strip()

    def get_article_img(self, article):
        figure = article.find("img")
        if not figure:
            return ""
        return figure['src']

    def get_articles(self) -> list:
        soup = self.get_soup(self.url)
        return soup.find_all("article", class_="article-min")
