from rest_framework.test import APIClient
from django.urls.base import reverse


def test_swagger_documentation():
    client = APIClient()
    response = client.get(reverse("swagger-ui"))
    assert response.status_code == 200


def test_redoc_documentation():
    client = APIClient()
    response = client.get(reverse("redoc"))
    assert response.status_code == 200


def test_get_schema():
    client = APIClient()
    response = client.get(reverse("schema"))
    assert response.status_code == 200
