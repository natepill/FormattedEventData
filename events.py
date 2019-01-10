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

        '''Need regex to grab the time from the date and price attributes'''

        print(response.css('div.search-main-content__events-list'))
        # for item in response.css('div.search-main-content__events-list').extract():
        #     event = Event()
        #     div_container = response.css('div.eds-media-card-content__content__principal')
        #
        #     event['title'] = div_container.css("a.eds-media-card-content__action-link h3.eds-media-card-content__title.eds-text-color--grey-800.eds-text-bl div.card-text--truncated__three::text").extract_first()
        #     event['date'] = div_container.css('div.eds-media-card-content__sub-content div.eds-text-bs--fixed.eds-text-color--grey-600.eds-l-mar-top-1::text').extract_first()
        #     event['location'] = div_container.css('div.eds-media-card-content__sub-content div.eds-media-card-content__sub-content-cropped div.eds-text-bs--fixed.eds-text-color--grey-600.eds-l-mar-top-1 div.card-text--truncated__one::text').extract_first()
        #     event['price'] = div_container.css('div.eds-media-card-content__sub-content div.eds-media-card-content__sub-content-cropped div.eds-text-bs--fixed.eds-text-color--grey-600.eds-l-mar-top-1::text').extract_first()
        #
        #     return event
