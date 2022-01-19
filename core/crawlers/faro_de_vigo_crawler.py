import urllib.parse

from core.models import Article

from .common import CrawlerBase


class FaroDeVigoCrawler(CrawlerBase):
    source = Article.FARO_DE_VIGO
    url_base = "https://galego.farodevigo.es/"
    url = urllib.parse.urljoin(url_base, "celta-de-vigo/")

    def get_article_url(self, article) -> str:
        return f'{self.url_base}{article.find(class_="new__headline")["href"]}'

    def get_article_title(self, article) -> str:
        return article.find(class_="new__headline").text.strip()

    def get_article_img(self, article):
        picture_node = article.find("picture")
        if not picture_node:
            return ""
        return picture_node.get("src")

    def get_articles(self) -> list:
        soup = self.get_soup(self.url)
        articles = soup.find_all("article", class_="new")
        celta_articles = []
        for article in articles:
            if article.select('a[href="/celta-de-vigo/"]'):
                celta_articles.append(article)
        return celta_articles
