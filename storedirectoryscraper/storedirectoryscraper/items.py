# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from storemapapp.models import Ruc


class RucItem(DjangoItem):
    django_model = Ruc
