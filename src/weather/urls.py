from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("forecast/", views.forecast, name="forecast"),
    path("archive/", views.archive, name="archive"),
]
