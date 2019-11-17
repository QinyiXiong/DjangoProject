from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class CrawlerxyzgConfig(AppConfig):
    name = 'CrawlerXYZG'

    def ready(self):
        autodiscover_modules('sayhellow.py')
