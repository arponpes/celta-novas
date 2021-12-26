import pytest
from core.crawlers.common import CrawlerBase


class TestCrawlerBase:
    @pytest.mark.django_db
    def test_normalize_url(self):
        assert CrawlerBase.normalize_url("www.foo.com/foo") == "https://www.foo.com/foo"
