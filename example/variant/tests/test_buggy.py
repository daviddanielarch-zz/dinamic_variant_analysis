import pytest

pytestmark = pytest.mark.django_db


def test_buggy(client):
    response = client.get('/buggy')
    assert response.status_code == 200
