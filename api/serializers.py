from rest_framework import serializers

from core.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "url", "source", "image_url", "created_at")
