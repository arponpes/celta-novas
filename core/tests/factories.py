import factory
import factory.fuzzy

from core.models import New

source_choices = [s[0] for s in New.SOURCE_CHOICES]


class NewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = New

    title = factory.Faker('text')
    url = factory.Faker('url')
    source = factory.fuzzy.FuzzyChoice(choices=source_choices)
    created_at = factory.Faker('date')
