
import scrapy
from scrapy.item import Item, Field


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    populator = scrapy.Field()


class Spider3(scrapy.Spider):
    name = "imbd-spider"
    allowed_domains = ['imbd.com']
    start_urls = ['https://www.imbd.com/chart/top']


    def parse(self, response):
        item = NewItem()
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        item['project'] = self.settings.get('BOT-NAME')
        item['spider'] = self.name

        return item
