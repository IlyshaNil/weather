from django.db import models


class WeatherArchive(models.Model):
    region = models.TextField(null=True, blank=True)
    date = models.DateField()
    day_temp = models.DecimalField(max_digits=4, decimal_places=2)
    night_temp = models.DecimalField(max_digits=4, decimal_places=2)
    humidity = models.IntegerField()

    def __str__(self):
        return f'{self.region} {self.date}'