# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table = 'douban_top250'#Mysql表
    image=scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    introduction=scrapy.Field()
    content=scrapy.Field()
    son_url=scrapy.Field()
    score = scrapy.Field()
    people = scrapy.Field()
    words = scrapy.Field()
