from django.test import TestCase

from .factories import NewFactory
from ..models import New


class NewTest(TestCase):
    def test_a_b_test_creation(self):
        new_test = NewFactory()

        self.assertEqual(isinstance(new_test, NewTest), True)
