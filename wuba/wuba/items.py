# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    huxing = scrapy.Field()
    add = scrapy.Field()
    price = scrapy.Field()
    det = scrapy.Field()
    link = scrapy.Field()
    chaoxiang = scrapy.Field()
    xiaoqu = scrapy.Field()
    time = scrapy.Field()
