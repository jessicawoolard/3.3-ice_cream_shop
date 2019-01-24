from django.apps import AppConfig
from django.contrib import admin
from .models import Image

admin.site.register(Image)


class IceCreamShopConfig(AppConfig):
    name = 'ice_cream_shop'
