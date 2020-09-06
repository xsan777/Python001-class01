# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    n_star = scrapy.Field()
    estimate = scrapy.Field()
    sentiment = scrapy.Field()
                
                
