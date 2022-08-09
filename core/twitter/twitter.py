import tweepy
from django.conf import settings


class TwitterModule:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=settings.API_KEY,
            consumer_secret=settings.API_KEY_SECRET,
            access_token=settings.ACCESS_TOKEN,
            access_token_secret=settings.ACCESS_TOKEN_SECRET,
        )

    def create_tweet(self, article):
        article_text = f"""
        {article.title}
        {article.url}
        """
        self.client.create_tweet(article_text)
