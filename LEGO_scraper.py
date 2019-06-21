#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ["https://brickset.com/sets/year-2019"]
    
    def parse(self,response):
        SET_SELECTOR = '.set'  # grab sets on the page,sets stored in class sets
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'  # each set is stored within an h1 tag
            PRICE_SELECTOR = './/dl[dt/text() = "RRP"]/dd/text()'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            ID_SELECTOR = './/h1/a/span/text()'
            RATE_SELECTOR = '//div[@class="rating"]/@title'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(), # name of sets
                'price': brickset.xpath(PRICE_SELECTOR).extract(),
	'piece': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'set_ID': brickset.xpath(ID_SELECTOR).extract_first(),
                'rating': brickset.xpath(RATE_SELECTOR).extract_first()
            }
        # keep searching for the next page
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse)

