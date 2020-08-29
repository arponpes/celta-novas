from django.db import models


POSITIONS = (
    ('GK', 'Portero'),
    ('DC', 'Central'),
    ('FBL', 'Lateral izquierdo'),
    ('FBR', 'Lateral derecho'),
    ('DC', 'Centrocampista'),
    ('MC', 'Medio centro'),
    ('AML', 'Media punta izquierda'),
    ('AMR', 'Media punta derecha'),
    ('AMC', 'Media punta centro'),
    ('ST', 'Delantero')
)

OPINION = (
    ('A', 'G.O.A.T'),
    ('B', 'TOP'),
    ('C', 'Gostoso'),
    ('D', 'Not bad'),
    ('E', 'Pocho'),
    ('F', 'Muy pocho')
)

class Player(models.Model):
    name = models.CharField('Nombre', max_length=50)
    position = models.CharField('Posicion', max_length=50, choices=POSITIONS)
    image = models.ImageField('Image', blank=True, null=True)
    notes = models.TextField('Notas', blank=True, null=True)
    opinion = models.CharField(
        'Opinion', max_length=50, choices=OPINION , blank=True, null=True
    )

    def __str__(self):
        return f'{self.name}'
