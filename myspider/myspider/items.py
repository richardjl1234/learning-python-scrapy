# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()


if __name__ == "__main__":
    item = MyspiderItem()
    item['name'] = 'xxx'
    print(item)