import urllib.parse

from core.models import Article

from .common import CrawlerBase
from .mixings import CrawlerMixin


class FaroDeVigoCrawler(CrawlerBase, CrawlerMixin):
    source = Article.FARO_DE_VIGO
    url_base = "https://galego.farodevigo.es/"
    url = urllib.parse.urljoin(url_base, "celta-de-vigo/")

    def get_article_url(self, article) -> str:
        return f'{self.url_base}{article["href"]}'

    def get_article_title(self, article) -> str:
        return article.text.strip()

    def get_articles(self) -> list:
        soup = self.get_soup(self.url)
        articles = soup.find_all("article", class_="new")
        celta_articles = []
        for article in articles:
            if article.select('a[href="/celta-de-vigo/"]'):
                celta_articles.append(article.find_all(class_="new__headline")[0])
        return celta_articles
