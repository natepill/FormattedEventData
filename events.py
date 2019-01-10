import scrapy
from scrapy.item import Item, Field


class Event(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()



class QuotesSpider(scrapy.Spider):
    name = "events"


    def start_requests(self):
        """ Returns an iterable of requests, can be a list of requests or a generator function"""

        urls = [
            'https://www.eventbrite.com/d/ca--san-francisco/business--events/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        event = Event()
        event['tite'] = response.css('eds-media-card-content__primary-content').extract()
        event['date'] =
        # item['date'] = response.css('//title/text()').extract()
        # item['location'] = response.css)()
        # item['price'] = self.settings.css('BOT-NAME')
        # item['time'] = self.name

        return item
