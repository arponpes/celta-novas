import requests
from bs4 import BeautifulSoup
from datetime import datetime
from url_normalize import url_normalize

from core.models import Article


class CrawlerBase:
    source = None
    url_base = None
    url = None
    DEFAULT_IMAGE = "default_image_url"  # Replace with a default image URL

    def get_articles(self) -> list:
        raise NotImplementedError

    def get_article_url(self, article) -> str:
        raise NotImplementedError

    def get_article_title(self, article) -> str:
        raise NotImplementedError

    def get_article_img(self, article):
        pass

    def get_soup(self, url):
        page_content = self.make_requests(url)
        return BeautifulSoup(page_content, "html.parser")

    def normalize_url(self, url):
        return url_normalize(url)

    def make_requests(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return ""

    def check_article_extracted_correctly(self, title, url):
        return all([title, url])

    def execute_crawler(self):
        articles_from_source = self.get_articles()
        articles = []
        for article in articles_from_source:
            title = self.get_article_title(article)
            url = self.normalize_url(self.get_article_url(article))
            if not self.check_article_extracted_correctly(title, url):
                continue
            articles.append(
                Article(
                    title=title,
                    url=url,
                    image_url=self.get_article_img(article) or self.DEFAULT_IMAGE,
                    source=self.source,
                    created_at=datetime.now(),  # Replacing timezone.now()
                )
            )
        return articles
