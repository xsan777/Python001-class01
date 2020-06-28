# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class MaoYanItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_type = scrapy.Field()
    movie_up_time = scrapy.Field()