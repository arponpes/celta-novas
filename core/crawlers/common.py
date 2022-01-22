import requests
from bs4 import BeautifulSoup
from core.models import Article
from django.conf import settings
from url_normalize import url_normalize


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

    def get_article_img(self, article):
        pass

    def update_articles(self, articles):
        for article in articles:
            url = self.normalize_url(self.get_article_url(article))
            title = self.get_article_title(article)
            image_url = self.get_article_img(article) or settings.DEFAULT_IMAGE
            if not self.to_be_created(title, url):
                continue

            Article(title=title, url=url, image_url=image_url, source=self.source).save()

    @staticmethod
    def normalize_url(url):
        return url_normalize(url)

    def execute_crawler(self):
        articles = self.get_articles()
        self.update_articles(articles)

    def to_be_created(self, title, url):
        if Article.objects.filter(title=title).exists() or Article.objects.filter(url=url).exists():
            return False
        return True

    def get_soup(self, url):
        page_content = self.make_requests(url)
        return BeautifulSoup(page_content, "html.parser")

    def make_requests(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return ""
