from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.eventbrite.com/d/ca--san-francisco/business--events/').text #grabs text (html) from response object
soup = BeautifulSoup(source, 'lxml')


unordered_list_tag = soup.find('ul', class_='search-main-content__events-list')
list_of_events = unordered_list_tag.find_all('li')

event_titles = list()
locations = list()
dates = list()
prices = list()

for event in list_of_events:
    try:
        event_titles.append(event.find('div', class_='card-text--truncated__three'))
    except:
        event_titles.append(None)

    try:
        dates.append(event.find('div', class_='eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1'))
    except:
        dates.append(None)

    try:
        locations.append(event.find('div', class_='card-text--truncated__one'))
    except:
        locations.append(None)


    try:
        prices.append(event.find_all('div', class_='eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1'))
    except:
        prices.append(0)


# for date in dates:
#     print(date.text)


for items in prices:
    for price in items:
        print(price.text)



# print(dates)







# print(unordered_list_tag)
# print(list_of_events)


# try:
#     event_titles = soup.find('ul', class_='card-text--truncated__three')
# except Exception as e:
