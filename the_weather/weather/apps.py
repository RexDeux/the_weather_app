from django.apps import AppConfig
from django.urls import re_path

class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
