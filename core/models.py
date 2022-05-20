from django.db import models


class Article(models.Model):
    MARCA = "MARCA"
    MOI_CELESTE = "MOI CELESTE"
    LA_VOZ_DE_GALICIA = "LA VOZ DE GALICIA"
    FARO_DE_VIGO = "FARO DE VIGO"

    SOURCE_CHOICES = (
        (MARCA, "Marca"),
        (MOI_CELESTE, "Moi celeste"),
        (LA_VOZ_DE_GALICIA, "La voz de Galicia"),
        (FARO_DE_VIGO, "Faro de Vigo"),
    )

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    image_url = models.CharField(max_length=1000, null=True)
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.source}"

    class Meta:
        indexes = [
            models.Index(name="article_source_index", fields=["title", "-created_at"]),
        ]
