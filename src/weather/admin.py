from django.contrib import admin
from .models import WeatherArchive


@admin.register(WeatherArchive)
class WeatherArchiveAdmin(admin.ModelAdmin):
    list_display = ["region", "date"]
