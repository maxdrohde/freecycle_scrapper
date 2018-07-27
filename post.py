# A class to represent a FreeCycle post

import re
import requests
from bs4 import BeautifulSoup
from tools import make_alpha, make_numeric
from get_ids import get_ids

BASE_STRING = 'https://groups.freecycle.org/group/WashingtonDC/posts/'

def get_location_and_date(soup):
    detail = soup.find('div', id="post_details")
    children = [x.text for x in detail.children if len(str(x)) > 3]
    location = children[0].split(':')[1].strip()
    date = children[1].split(':')[1].strip()
    return location, date

def get_description(soup):
    detail = soup.find('div', id="group_post")
    desc = detail.find('p').text.strip()
    return desc

def get_title(soup):
    headers  = soup.findAll('header')
    title = [x.text for x in headers if 'OFFER' in x.text][0]
    title = title.split('OFFER:')[1].strip()
    return title

class Post():

    def __init__(self, id):

        self.id = id
        self.url = BASE_STRING + id
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        location_date = get_location_and_date(self.soup)
        self.location = location_date[0]
        self.date = location_date[1]

        self.description = get_description(self.soup)
        self.title = get_title(self.soup)

        self.coordinates = None


    def __repr__(self):
        return(f'Title: {self.title} | Location: {self.location} | ID: {self.id} | Date: {self.date}')

    def __str__(self):
        return(f'Title: {self.title} | Location: {self.location} | ID: {self.id} | Date: {self.date}')

#### TESTING ####

print ('#### Starting scraping ####')
print ('###########################')
ids = get_ids()
print(f'There are {len(ids)} ids')
print()

post_list = []
for i, x in enumerate(ids):
    print(f'Processing post number {i} of {len(ids)}')
    try:
        post_list.append(Post(x))
    except:
        print(f'An error occured in post {i}')
