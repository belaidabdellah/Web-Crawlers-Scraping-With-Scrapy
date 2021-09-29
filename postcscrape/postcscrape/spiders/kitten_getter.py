import scrapy


class KittenGetterSpider(scrapy.Spider):
    name = 'kitten_getter'
    allowed_domains = ['reddit.com/r/cats']
    start_urls = ['http://reddit.com/r/cats/']

    def parse(self, response):
        pass
