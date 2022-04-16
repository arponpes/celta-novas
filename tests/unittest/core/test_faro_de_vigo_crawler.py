from core.crawlers.faro_de_vigo_crawler import FaroDeVigoCrawler
from core.models import Article
from tests.unittest.conftest import CommonTest
import pytest


class TestFaroDeVigoCrawler(CommonTest):
    crawler = FaroDeVigoCrawler()
    fixture = "tests/unittest/core/fixtures/faro_de_vigo.html"

    @pytest.mark.django_db
    def test_get_article_url(self, mock_response):
        expected_url = (
            "https://galego.farodevigo.es//celta-de-vigo/2022/01/19/celta-logra-triunfo-madurez-frente-61747882.html"
        )
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_url(articles[0]) == expected_url

    @pytest.mark.django_db
    def test_get_article_title(self, mock_response):
        expected_title = "El Celta firma un triunfo de madurez"
        articles = self.crawler.get_articles()
        assert self.crawler.get_article_title(articles[0]) == expected_title

    @pytest.mark.django_db
    def test_get_articles(self, mock_response):
        articles = self.crawler.get_articles()
        assert len(articles) == 17

    @pytest.mark.django_db
    def test_update_articles(self, mock_response):
        articles = set(self.crawler.get_articles())
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 17

    @pytest.mark.django_db
    def test_update_articles_avoid_duplicates(self, mock_response):
        articles = self.crawler.get_articles()
        assert Article.objects.count() == 0
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 17
        self.crawler.update_articles(articles)
        assert Article.objects.count() == 17

    @pytest.mark.django_db
    def test_get_article_image(self, mock_response):
        articles = self.crawler.get_articles()
        assert (
            self.crawler.get_article_img(articles[0]).strip() == "https://estaticos-cdn.prensaiberica.es/clip/"
            "eee3962b-a83e-4d3f-8da3-5c838d59f61c_21-9-aspect-ratio_default_0_x2278y1104.jpg"
        )
