from django.db import models


class New(models.Model):

    SOURCE_CHOICES = (
        ('MR', 'MARCA'),
        ('MC', 'MOI CELESTE'),
        ('VG', 'LA VOZ DE GALICIA'),
        ('FV', 'FARO DE VIGO')
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
