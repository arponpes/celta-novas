from datetime import timedelta, date

from core import models
from django.db.models import Count
from django.utils import timezone


class ArticleMetricsGenerator:
    def __init__(self, articles) -> None:
        self.articles = articles

    def __call__(self) -> dict:
        articles_metrics = {}
        articles_metrics["total_articles"] = self.get_total_articles()

        articles_metrics["articles_last_24_hours"] = self.get_articles_last_24_hours()

        articles_metrics["source_with_more_articles"] = self.get_source_with_more_articles()

        articles_metrics["source_with_more_articles_last_24_hours"] = self.get_source_with_more_articles_last_24_hours()

        articles_metrics["articles_by_source"] = self.get_articles_by_source()

        from_date, to_date = self.last_week_date_range()
        articles_metrics["articles_last_week_by_date"] = self.get_articles_by_date(from_date, to_date)
        articles_metrics["articles_last_week_by_date_by_source"] = self.get_articles_by_date_by_source(from_date)

        return articles_metrics

    def get_total_articles(self) -> int:
        return self.articles.count()

    def get_articles_last_24_hours(self) -> int:
        return self.articles.filter(created_at__gt=timezone.now() - timedelta(hours=24)).count()

    def get_source_with_more_articles(self) -> dict:
        source_with_more_articles = self.articles.values("source").annotate(Count("source")).order_by("-source__count")
        if source_with_more_articles:
            return source_with_more_articles[0]
        return {"source": "", "source__count": 0}

    def get_source_with_more_articles_last_24_hours(self) -> dict:
        source_with_more_articles_last_24_hours = (
            self.articles.filter(created_at__gte=timezone.now() - timedelta(hours=24))
            .values("source")
            .annotate(Count("source"))
            .order_by("-source__count")
        )
        if source_with_more_articles_last_24_hours:
            return source_with_more_articles_last_24_hours[0]
        return {"source": "", "source__count": 0}

    def get_articles_by_source(self) -> dict:
        articles_by_source = {}
        for source in models.Article.SOURCE_CHOICES:
            articles_by_source[source[0]] = self.articles.filter(source=source[0]).count()
        return articles_by_source

    def get_articles_by_date(self, start_date, end_date) -> dict:
        return (
            self.articles.filter(created_at__gte=start_date)
            .values("created_at__date")
            .annotate(count=Count("id"))
            .values("created_at__date", "count")
            .order_by("created_at__date")
        )

    def get_articles_by_date_by_source(self, start_date) -> dict:
        articles_by_date_by_source = {}
        for source in models.Article.SOURCE_CHOICES:
            articles_by_date_by_source[source[0]] = (
                self.articles.filter(created_at__gte=start_date, source=source[0])
                .values("created_at__date")
                .annotate(count=Count("id"))
                .values("created_at__date", "count")
                .order_by("created_at__date")
            )
        return articles_by_date_by_source

    def last_week_date_range(self) -> tuple:
        today = date.today()
        start_date = today - timedelta(days=7)
        end_date = today
        return start_date, end_date
