from django.db.models import Count
from django.utils import timezone
from datetime import timedelta


class ArticleMetricsGenerator:
    def __init__(self, articles) -> None:
        self.articles = articles

    def __call__(self) -> dict:
        articles_metrics = {}
        articles_metrics['total_articles'] = self.get_total_articles()

        articles_metrics[
            'articles_last_24_hours'
        ] = self.get_articles_last_24_hours()

        # TODO fix case no articles

        articles_metrics[
            'source_with_more_articles'
        ] = self.get_sources_with_more_metrics()

        articles_metrics[
            'source_with_more_articles'
        ] = self.get_source_with_more_articles()

        articles_metrics['source_with_more_articles_last_24_hours'] = \
            self.get_source_with_more_articles_last_24_hours()
        return articles_metrics

    def get_sources_with_more_metrics(self) -> int:
        return self.articles.values('source').annotate(
            Count('source')
        ).order_by('-source__count')[0]

    def get_total_articles(self) -> int:
        return self.articles.count()

    def get_articles_last_24_hours(self) -> int:
        return self.articles.filter(
            created_at__gt=timezone.now() - timedelta(hours=24)
        ).count()

    def get_source_with_more_articles(self) -> int:
        return self.articles.values(
                'source'
            ).annotate(
                Count('source')
            ).order_by('-source__count')[0]

    def get_source_with_more_articles_last_24_hours(self) -> int:
        return self.articles.filter(
                    created_at__gte=timezone.now() - timedelta(hours=24)
                ).values(
                    'source'
                ).annotate(
                    Count('source')
                ).order_by('-source__count')[0]
