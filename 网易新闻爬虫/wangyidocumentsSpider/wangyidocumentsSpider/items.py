# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyidocumentsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    path = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    source = scrapy.Field()
    text = scrapy.Field()
    editor = scrapy.Field()
    link = scrapy.Field()
    pass


