import scrapy
from scrapy.item import Item, Field
from bs4 import BeautifulSoup as bso



# import xml.etree.ElementTree as ET



# from selenium import webdriver
# driver = webdriver.Firefox()
# test = driver.get("https://www.eventbrite.com/d/ca--san-francisco/business--events/")
# print(test)



# from bs4 import BeautifulSoup
#
#     with open(url[0]) as f:
#         soup = BeautifulSoup(f, 'html')
#
#     results = soup.find_all('div')
#


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
            'https://www.eventbrite.com/d/ca--san-francisco/all-events/?page=1&tags=Training'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)


    def parse(self, response):

        '''Need regex to grab the time from the date and price attributes'''

        # print(response.css('ul.search-main-content__events-list').extract())

        ul_selector = response.css("ul.search-main-content__events-list").extract_first()

        soup = bso(ul_selector, "lxml")
        unordered_list = soup.find("ul")

        print(unordered_list)
        # print(first_child.findChildren())
        list_of_tags = unordered_list.children
        # print(list_of_tags)

        all_events = list()

        # print(list_of_tags)

        for item in list_of_tags:
            event = Event()
            div_container = response.css('div.eds-media-card-content__content__principal')
            # print(div_container)
            event['title'] = div_container.css("a.eds-media-card-content__action-link h3.eds-media-card-content__title.eds-text-color--grey-800.eds-text-bl div.card-text--truncated__three::text").extract_first()
            event['date'] = div_container.css('div.eds-media-card-content__sub-content div.eds-text-bs--fixed.eds-text-color--grey-600.eds-l-mar-top-1::text').extract_first()
            event['location'] = div_container.css('div.eds-media-card-content__sub-content div.eds-media-card-content__sub-content-cropped div.eds-text-bs--fixed.eds-text-color--grey-600.eds-l-mar-top-1 div.card-text--truncated__one::text').extract_first()
            event['price'] = div_container.css('div.eds-media-card-content__sub-content div.eds-media-card-content__sub-content-cropped div.eds-text-bs--fixed.eds-text-color--grey-600.eds-l-mar-top-1::text').extract_first()

            return event
            # all_events.append(event)


        # print('ALL EVENTS: ')
        # print(all_events)


        # print(all_events)
        # return all_events
