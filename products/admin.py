# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, Category, Image, ImageAlbum

admin.site.register(Product)

admin.site.register(Category)

admin.site.register(Image)

admin.site.register(ImageAlbum)