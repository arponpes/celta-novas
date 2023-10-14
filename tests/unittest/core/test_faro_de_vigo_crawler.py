import pytest

from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.models import Article
from tests.unittest.conftest import CommonTest


class TestFaroDeVigoCrawler(CommonTest):
    crawler = FaroDeVigoCrawler()
    fixture = "tests/unittest/core/fixtures/faro_de_vigo.html"

    @pytest.mark.django_db
    def test_get_article_url(self):
        expected_url = (
            "https://galego.farodevigo.es//celta-de-vigo/2022/01/19/celta-logra-triunfo-madurez-frente-61747882.html"
        )
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self):
        expected_title = "El Celta firma un triunfo de madurez"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_title(articles[0]) == expected_title

    @pytest.mark.django_db
    def test_get_articles(self):
        articles = self.crawler.get_articles()
        assert len(articles) == 17

    @pytest.mark.django_db
    def test_get_article_image(self):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip() == "https://estaticos-cdn.prensaiberica.es/clip/"
            "eee3962b-a83e-4d3f-8da3-5c838d59f61c_21-9-aspect-ratio_default_0_x2278y1104.jpg"
        )

    @pytest.mark.django_db
    def test_execute_crawler(self):
        articles = self.crawler.execute_crawler()
        assert len(articles) == 17
        for article in articles:
            assert article.source == Article.FARO_DE_VIGO
            assert article.url
            assert article.title
