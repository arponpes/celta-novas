from core.models import Article
from url_normalize import url_normalize

from .utils import to_be_created


class CrawlerBase:
    source = None
    url_base = None
    url = None

    def get_articles(self) -> list:
        raise NotImplementedError

    def get_article_url(self, article) -> str:
        raise NotImplementedError

    def get_article_title(self, article) -> str:
        raise NotImplementedError

    def update_articles(self, articles):
        for article in articles:
            url = self.normalize_url(self.get_article_url(article))
            title = self.get_article_title(article)
            if not to_be_created(title, url):
                continue

            Article(title=title, url=url, source=self.source).save()

    @staticmethod
    def normalize_url(url):
        return url_normalize(url)

    def execute_crawler(self):
        articles = self.get_articles()
        self.update_articles(articles)
