from django.contrib import admin

from core.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "source")
    list_filter = ("source",)
