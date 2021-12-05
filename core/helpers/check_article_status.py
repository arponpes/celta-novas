from core.models import Article
from django.utils import timezone
from datetime import timedelta


def check_article_status():
    for source in Article.SOURCE_CHOICES:
        if Article.objects.filter(
            source=source[0],
            created_at__gt=timezone.now() - timedelta(hours=24)
        ).count() == 0:
            return False
    return True
