from django.db import models


class New(models.Model):
    MARCA = 'MARCA'
    MOI_CELESTE = 'MOI CELESTE'
    LA_VOZ_DE_GALICIA = 'LA VOZ DE GALICIA'
    FARO_DE_VIGO = 'FARO DE VIGO'

    SOURCE_CHOICES = (
        ('MR', MARCA),
        ('MC', MOI_CELESTE,
        ('VG', LA_VOZ_DE_GALICIA),
        ('FV', FARO_DE_VIGO)
    )

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    source = models.CharField(
        max_length=2,
        choices=SOURCE_CHOICES
    )
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.source}'
