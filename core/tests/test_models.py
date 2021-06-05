import pytest
from .factories import NewFactory
from core.models import New


@pytest.mark.django_db
def test_new_test_creation():
    new_test = NewFactory()
    assert isinstance(new_test, New)
