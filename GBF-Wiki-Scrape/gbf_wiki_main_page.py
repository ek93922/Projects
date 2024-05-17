from msilib.schema import tables
import requests
from bs4 import BeautifulSoup
import calendar
import time
from datetime import datetime
import math
import os
import pathlib

BASE_URL = "https://gbf.wiki/Main_Page"

try:
    # response = requests.get(BASE_URL)
    # page_content = response.text
    # soup = BeautifulSoup(page_content, "lxml")

    # #Extracts the page as local file
    # with open('main_page.html', 'wb+') as file:
    #     file.write(response.content)

    dirname = os.path.dirname(__file__)
    html_file = os.path.join(dirname, '', 'main_page.html')
    with open(html_file, 'rb') as file:
        soup = BeautifulSoup(file.read(), 'lxml')

    # Defines current time in form of Dynamic Timestamp
    gmt = time.gmtime()
    timestamp = calendar.timegm(gmt)

#------------------------------------------------------------------------------------------------------#
    # * Current Events *

    # Find and print all current events
    for td in soup.findAll('td', {'style': 'vertical-align: top; text-align: center;'}):
        cur_evt_list = []
        for img in td.findAll('img'):
            evt = img.get('alt')

            # Prevents duplicate entries in case same event has multiple banners img
            if evt not in cur_evt_list:
                cur_evt_list.append(evt)
        
        # Creates 2 lists that keeps track of start timestamps and end timestamps
        start_time = []
        end_time = []
        for span in td.findAll('span', {'class': 'localtime'}):
            start_time.append(span.get('data-start'))
            end_time.append(span.get('data-end'))


        # For showing current events. Check if the event has started or will start soon.
        # Use current dynamic timestamp and subtract start dynamic timestamp
        # If the value is - then it started, if the value is + then it will start soon.
        i = 0
        while i < len(cur_evt_list):
            delta = timestamp - int(start_time[i])
            ts1 = datetime.fromtimestamp(timestamp)

            if delta < 0:
                ts2 = datetime.fromtimestamp(int(start_time[i]))
                delta = ts2 - ts1
                d = delta.days
                h = math.trunc(delta.seconds/3600)
                if d < 1:
                    print(f'{cur_evt_list[i]} starts in {h}h')
                else:    
                    print(f'{cur_evt_list[i]} starts in {d}d {h}h')
            else:
                ts2 = datetime.fromtimestamp(int(end_time[i]))
                delta = ts2 - ts1
                d = delta.days
                h = math.trunc(delta.seconds/3600)
                if d < 1:
                    print(f'{cur_evt_list[i]} will end in {h}h (<t:{end_time[i]}:f>)')
                else:
                    print(f'{cur_evt_list[i]} will end in {d}d {h}h (<t:{end_time[i]}:f>)')
            i += 1

        


#------------------------------------------------------------------------------------------------------#
    # * UPCOMING EVENTS *
    
    # gbf.wiki's upcoming event td is identified with the last value of "style="vertical-align: top;""
    style_list = []

    # gbf.wiki's table format <td style="vertical-align: top;">
    for td in soup.find_all('td', {'style': 'vertical-align: top;'}):
        style_list.append(td)

    # Selects last td which contains upcoming event information as established previously 
    up_evt = style_list[len(style_list)- 1]
    up_evt_list = []
    
    # <a href="LINK TO NAME OF EVENT" title="NAME OF EVENT">
    for img in up_evt.findAll('img'):
        evt = img.get('alt')

        # Prevents duplicate entries in case same event has multiple banners img
        if evt not in up_evt_list:
            up_evt_list.append(evt)

    # Every odd entry is start time, even entry is end time
    times = []
    for span in up_evt.findAll('span', {'class': 'localtime'}):
        datatime = span.get('data-time')
        if datatime not in times:
            times.append(datatime)
    
    # Create a dictionary that uses event as key,
    # and a list of start and end date as values.
    up_evt_sch = {}
    for entry_name in up_evt_list:
        up_evt_time = []
        # First append/pop is Start date
        up_evt_time.append(times[0])
        times.pop(0)
        # Second append/pop is End date
        up_evt_time.append(times[0])
        times.pop(0)

        up_evt_sch[entry_name] = up_evt_time

    # Creates a string 
    for entry in up_evt_sch:
        event_name = entry
        start_date = up_evt_sch[event_name][0]
        print(f'{event_name} Starts on <t:{start_date}:f>')



#------------------------------------------------------------------------------------------------------#

except:
    print("Error has occurred.")
