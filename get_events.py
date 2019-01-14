from bs4 import BeautifulSoup
import requests
import csv
import re

soup = BeautifulSoup(source, 'lxml')
source = requests.get('https://www.eventbrite.com/d/ca--san-francisco/business--events/').text #grabs text (html) from response object



def construct_url(form_parameters):
    '''Need node app to structure request to be sent as an array of parameters'''
    '''Takes in array of parameters and constructs requested url'''


    '''Array needs to be a set size, or every field must be required or if no answer is given then a null value must be appended to the array'''

    url = 'https://www.eventbrite.com/d/{}/{}--{}--{}/{}'.format(form_parameters[0], form_parameters[1],form_parameters[2],form_parameters[3],form_parameters[4],form_parameters[5])
    # https://www.eventbrite.com/d/{location}/{category}--{event-type}--{date}/{page-number}
    return url



def fill_in_none_values(formatted_details):
    date_pattern = re.compile(r'\w\w\w, \w\w\w [0-9]?\d')
    # time_pattern = re.compile(r'[0-9]?\d:\d\d\w\w')
    # Will use time_pattern once we've ensured that formatted_details has all indexes filled
    location_pattern = re.compile(r'^[A-Z]$[A-Z]')
    price_pattern = re.compile(r'^Starts')
    price_pattern2 = re.compile(r'^Free')


    # index = 0
    for index, detail in enumerate(formatted_details):
        if index+2 >= len(formatted_details)-1:
            break

        if re.match(date_pattern, formatted_details[index]) == False:
            print("NO DATE")
            formatted_details.insert(index, 'None')

        if re.match(location_pattern, formatted_details[index+1]) == False:
            print("NO LOCATION")
            formatted_details.insert(index+1, 'None')

        if re.match(price_pattern, formatted_details[index+2]) == False or re.match(price_pattern2, formatted_details[index+2]) == False:
            print('NO PRICE')
            formatted_details.insert(index+2, 'None')

        # index += 1

    return formatted_details

                # date = date_pattern.finditer(list_of_events[1])
                # time = time_pattern.finditer(list_of_events[1])







# print(soup.find_all('li'))
try:
    event_titles = soup.find_all('div', class_='card-text--truncated__three')
    event_details = soup.find_all('div', class_='eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1')
except Exception as e:
    event_titles = None
    event_details = None

formatted_titles = list(filter(lambda x: x != '', map(lambda title: title.text, event_titles)))
formatted_details = list(filter(lambda x: x != '', map(lambda detail: detail.text, event_details)))


# print('{} \n'.format(formatted_details))

formatted_details = fill_in_none_values(formatted_details)

with open('formatted_details.txt', 'w') as file:
    file.write(str(formatted_details))
    # for detail in formatted_details:
    #     file.write(detail)

"""Prints out the price for every event"""
#TODO Throw test into a function
index = 2
for detail in formatted_details:
    print(formatted_details[index])
    if index >= len(formatted_details) - 3:
        break
    index += 3

""" Testing regex """
# date_pattern = re.compile(r'\w\w\w, \w\w\w [0-9]?\d')
# location_pattern = re.compile(r'^[A-Z]$[A-Z]')
# price_pattern = re.compile(r'^Starts')
# price_pattern2 = re.compile(r'^Free')
#
# print('REGEX Results: \n')
#
# if re.match(date_pattern, formatted_details[0]):
#     print(re.match(date_pattern, formatted_details[0])[0])
# if re.match(location_pattern, formatted_details[1]) == False:
#     print('location match')
# if re.match(price_pattern, formatted_details[index+2]) == False or re.match(price_pattern2, formatted_details[index+2]) == False:
#     print('price match')

"""Adding titles to events and creating an array of arrays containing event details"""
list_of_events = list()
index = 0
for event_title in formatted_titles:
    formatted_details.insert(index, event_title)
    list_of_events.append(formatted_details[index:index+4])
    index += 3

# print(formatted_details[0:4])
# for event in list_of_events:
#     print(event[3])
# print(list_of_events)



csv_file = open('event_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'date', 'time', 'location', 'price'])



"""Taking event details and  list of events """
# TODO: Maybe try to clean the data here

for event in list_of_events:
    time_pattern = re.compile(r'\d:\d\d\w\w')
    date_pattern = re.compile(r'\w\w\w, \w\w\w \d\d')
    price_pattern = re.compile(r'')

    title = list_of_events[0]
    date = date_pattern.finditer(list_of_events[1])
    time = time_pattern.finditer(list_of_events[1])
    location = list_of_events[2]
    price = list_of_events[3]
    csv_writer.writerow([title, date, time, location, price])

csv_file.close()




#
#
#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']
#         #to get value of an atrrtibute of a tag, we can access that attribute like a dict ^^
#         # print(vid_src)
#
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         print(vid_id)
#         #How to get really specific data like video id ^^
#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#
#     except Exception as e:
#             yt_link = None
#

#


#
# print(headline)

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml') #opening the html file and specifying the usage of the lxml bodyParser
#
#
# print(soup.prettyify()) #prints html that looks good
#


#find vs find_all: find method gets the first tag that matches the specification
#find_all method returns a list that matches all those arguments
