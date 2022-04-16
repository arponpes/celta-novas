from unittest.mock import Mock

import django
import pytest


def pytest_configure(config):
    django.setup()


class CommonTest:
    @pytest.fixture
    def mock_response(self, mocker):
        mock = Mock()
        mock.status_code = 200
        with open(self.fixture, "r") as f:
            mock.content = f.read()
        mocker.patch("requests.get", return_value=mock)
