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
    page_content = make_requests(url)
    return BeautifulSoup(page_content, 'html.parser')


def make_requests(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return ''
