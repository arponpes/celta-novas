from core.models import Article
from bs4 import BeautifulSoup
import requests


def to_be_created(title, url):
    if (
        Article.objects.filter(title=title).exists() or
        Article.objects.filter(url=url).exists()
    ):
        return False
    return True


def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
