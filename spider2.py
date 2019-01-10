import scrapy
from scrapy.item import Item, Field

class NewItem(scrapy.Item):
    main_headline = Field()
    headline = Field()

    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()




class Spider2(scrapy.Spider):
    name = "spider2"
    allowed_domains = ['www.superdatascience.com']
    start_urls = ['https://www.superdatascience.com']


    def parse(self, response):
        item = NewItem()
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        item['project'] = self.settings.get('BOT-NAME')
        item['spider'] = self.name

        return item
