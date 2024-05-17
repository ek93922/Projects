from textwrap import indent
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import os
import pathlib
import calendar
import time
import json
from datetime import datetime
import math
import re

BASE_URL = "https://gbf.wiki"
# Wiki Main Page is case sensitive
MAIN_PAGE = "Main_Page"

#------------------------------------------------------------------------------------------------------#
# * Current Events *
# Defines current time in form of Dynamic Timestamp
gmt = time.gmtime()
timestamp = calendar.timegm(gmt)

# Grabs json of main page
request_url = f"{BASE_URL}/api.php?action=parse&page={MAIN_PAGE}&format=json"
response = requests.get(request_url)
response = response.json()
jsonData = response['parse']['text']['*']
soup = BeautifulSoup(jsonData, 'lxml')
    # Find and print all current events
for td in soup.findAll("td", {"style": "vertical-align: top; text-align: center;"}):
    cur_evt_list = []
    for a in td.findAll("a"):
        evt = a.get("title")

        # Prevents duplicate entries in case same event has multiple banners img
        if evt not in cur_evt_list:
            cur_evt_list.append(evt)

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