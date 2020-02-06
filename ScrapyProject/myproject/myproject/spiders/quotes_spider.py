import scrapy
from scrapy.spiders import Spider

class QuotesSpider(Spider):
    name='quotes'
    start_urls={'http://quotes.toscrape.com/'}
    
    def parse(self, response):
        title=response.css('title').extract()
        yield{'titletext':title}
