from core.models import Article
from core.twitter.twitter import TwitterModule


class ArticleProcessor:
    def __init__(self, crawler_class):
        self.crawler_class = crawler_class
        self.twitter_module = TwitterModule()

    def process_articles(self):
        articles = self.crawler_class().execute_crawler()
        self.update_articles(articles)

    def update_articles(self, articles):
        for article in articles:
            if not self.to_be_created(article.title, article.url):
                continue
            self.save_article(article)
            self.create_tweet(article)

    def to_be_created(self, title, url):
        if Article.objects.filter(title=title).exists() or Article.objects.filter(url=url).exists():
            return False
        return True

    def save_article(self, article):
        article.save()

    def create_tweet(self, article):
        self.twitter_module.create_tweet(article.title, article.url)
