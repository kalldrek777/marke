# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Market777Item(scrapy.Item):
    img_url = scrapy.Field()


#
# class Model(scrapy.Item):
#     Product=Market777Item