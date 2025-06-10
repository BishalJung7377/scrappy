# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

### """""""""""" items are temporary data where we are storing out scrapped data """"""""""""
class ScrappyItem(scrapy.Item):
    ##this is to define our item container
    
    ## we have created temporary container to store the info from our spider
    quote_title = scrapy.Field()
    author_name = scrapy.Field()
    quote_tag = scrapy.Field()
    
