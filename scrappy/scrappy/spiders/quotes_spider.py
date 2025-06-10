# Define the spider code as a string

import scrapy

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
        
        all_div_quotes = response.css('div.quote')
        title = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css(".author::text").extract()
        tags = all_div_quotes.css(".tags::text").extract()
        yield {
            'quote_title' : title,
            'author_name' : author,
            'quote_tag': tags,
        }