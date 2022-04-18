from django.core.management import BaseCommand
from tests.unittest.core.factories import ArticleFactory
from core.models import Article
import random
from datetime import date
from datetime import timedelta


class Command(BaseCommand):
    """Django command to create fake data for development"""

    def handle(self, *args, **options):
        for _ in range(1000):
            article = ArticleFactory()
            article.created_at = date.today() - timedelta(days=random.randint(0, 365))
            article.save()

        self.stdout.write(self.style.SUCCESS("Successfully created fake data"))
