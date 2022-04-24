from django.urls import reverse, resolve


def test_main_url():
    path = reverse('main')
    assert resolve(path).view_name == 'main'


def test_forecast_url():
    path = reverse('forecast')
    assert resolve(path).view_name == 'forecast'


def test_archive_url():
    path = reverse('archive')
    assert resolve(path).view_name == 'archive'