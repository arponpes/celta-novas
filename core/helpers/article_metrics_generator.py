from datetime import timedelta

from core import models
from django.db.models import Count
from django.db.models.functions import TruncMonth
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

        date_one_week_ago = self.get_days_ago_date(7)
        date_one_year_ago = self.get_days_ago_date(365)
        articles_metrics["articles_last_week_by_date"] = self.get_articles_by_date(date_one_week_ago)
        articles_metrics["articles_last_week_by_date_by_source"] = self.get_articles_by_date_by_source(
            date_one_week_ago
        )
        articles_metrics["articles_last_year_by_date_by_source"] = self.get_articles_by_month_last_year(
            date_one_year_ago
        )
        articles_metrics["article_creation_trend"] = self.get_article_creation_trend()

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

    def get_articles_by_date(self, start_date) -> dict:
        return self.get_qs_by_date(created_at__gt=start_date)

    def get_articles_by_date_by_source(self, start_date) -> dict:
        articles_by_date_by_source = {}
        for source in models.Article.SOURCE_CHOICES:
            articles_by_date_by_source[source[0]] = self.get_qs_by_date(created_at__gt=start_date, source=source[0])
        return articles_by_date_by_source

    def get_qs_by_date(self, **kwargs) -> list:
        return list(
            self.articles.filter(**kwargs)
            .values("created_at__date")
            .annotate(count=Count("id"))
            .values("created_at__date", "count")
            .order_by("created_at__date")
        )

    def get_articles_by_month_last_year(self, start_date):
        return list(
            self.articles.filter(created_at__gt=start_date)
            .annotate(month=TruncMonth("created_at"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )

    def get_days_ago_date(self, days_ago) -> tuple:
        return (timezone.now() - timedelta(days=days_ago)).date()

    def get_article_creation_trend(self):
        articles_previous_month = self.articles.filter(
            created_at__gt=timezone.now() - timedelta(days=60), created_at__lt=timezone.now() - timedelta(days=30)
        ).count()
        articles_current_month = self.articles.filter(created_at__gt=timezone.now() - timedelta(days=30)).count()
        return (articles_previous_month / articles_current_month) * 100
