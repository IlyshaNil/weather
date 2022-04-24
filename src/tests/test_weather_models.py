from weather.models import WeatherArchive
import datetime as dt
import pytest

@pytest.mark.django_db
def test_weatherArchive_model():
    record = WeatherArchive.objects.create(
        region = 'region',
        date = dt.date(2022, 4, 1),
        day_temp = '27',
        night_temp = -1,
        humidity = 50
    )

    assert record.region == 'region'
    assert record.__str__() == 'region 2022-04-01'
    assert isinstance(record, WeatherArchive)
    