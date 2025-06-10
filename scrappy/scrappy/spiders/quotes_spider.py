# Define the spider code as a string

import scrapy
from ..items import ScrappyItem ## inheritance of the items class properties


class QuoteSpidr(scrapy.Spider):
    name = 'quotes' ## this is the name of our spider ## to run the spider we need this name
    ## spider crawl {name}
    start_urls = [ ## we can use list to pass multiple url in the spider
        'https://quotes.toscrape.com/'
    ]
    
    def parse(self, response): ### parse method to get the response from the url
        # title = response.css('title::text').extract() ## :: tells scrapy to get text inside title
        ## .extract() extract only the actual class data (only one)
        # yield { ## yield is used with generator and it bascially works like return
        #     'titletext' : title,
        # }
        
        items = ScrappyItem() 
        
        all_div_quotes = response.css('div.quote')
        
        for quotes in all_div_quotes: ## looping through all text in the website
            title = quotes.css('span.text::text').extract()
            author = quotes.css("small.author::text").extract()
            tags = quotes.css("a.tag::text").extract()
            ## yield is used with generator and it bascially works like return
            
            ## using inheritance to store title, author and tags name in the items class
            items['quote_title'] = title
            items['author_name'] = author
            items['quote_tag'] = tags
            
            yield  items ##al of the items returned properly