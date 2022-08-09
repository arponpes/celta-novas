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

    def create_tweet(self, title, url):
        article_text = f"""
        {title}
        {url}
        """
        self.client.create_tweet(text=article_text)
