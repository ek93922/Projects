from textwrap import indent
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup # pip install beautifulsoup4
import os
import pathlib
import calendar
import time
import json
from datetime import datetime
import math
import re
from titlecase import titlecase

BASE_URL = "https://gbf.wiki"
# Character search 
SEARCH = re.sub('\s+', '%20', input('Search? ').strip())

# Points to the json file to be usable for debugging purposes
# dirname = os.path.dirname(__file__)
# json_file = os.path.join(dirname, '', 'main_page.json')

# with open(json_file, 'rb') as file:
#     jsonData = json.load(file)
#     jsonData = jsonData['parse']['text']['*']
#     soup = BeautifulSoup(jsonData, 'lxml')


input_url = f'{BASE_URL}/api.php?action=parse&format=json&title={SEARCH}&redirects=1'

response = requests.get(input_url)
responseData = response.json()
PAGE_ID = responseData['parse']['pageid']

if PAGE_ID == 0:
    exit('Cannot find what you\'re looking for. Please try again.')

target_url = f'{BASE_URL}/api.php?action=parse&format=json&pageid={PAGE_ID}'
response = requests.get(target_url)
targetData = response.json()
targetData = targetData['parse']['text']['*']
soup = BeautifulSoup(targetData, 'lxml')

if soup.find('div').get('class').__contains__('table-container weapon character'):
    print('weapon')
   

#------------------------------------------------------------------------------------------------------#


    


