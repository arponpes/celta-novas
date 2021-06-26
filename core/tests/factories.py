import factory
import factory.fuzzy

from core.models import Article

source_choices = [s[0] for s in Article.SOURCE_CHOICES]


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Sequence(lambda n: 'Title %s' % n)
    url = factory.Sequence(lambda n: 'Url %s' % n)
    source = factory.fuzzy.FuzzyChoice(choices=source_choices)
    created_at = factory.Faker('date')
