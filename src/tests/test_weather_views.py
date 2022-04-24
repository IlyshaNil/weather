from django.test import Client
from django.urls import reverse, resolve


def test_main_view():
    url = reverse('main')
    response = Client().get(url)

    assert response.status_code == 200


def test_forecast_view():
    url = reverse('forecast')
    response = Client().get(url)

    assert response.status_code == 200


def test_archive_view():
    url = reverse('archive')
    response = Client().get(url)

    assert response.status_code == 200
    