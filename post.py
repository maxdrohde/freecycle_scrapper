# A class to represent a FreeCycle post

import requests
from bs4 import BeautifulSoup
from get_ids import get_ids
from parse_soup import get_description, get_title, get_location_and_date
from dateutil import parser

BASE_STRING = 'https://groups.freecycle.org/group/WashingtonDC/posts/'

class Post():

    def __init__(self, id):

        self.id = id
        self.url = BASE_STRING + id
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        location_date = get_location_and_date(self.soup)
        self.location = location_date[0]
        self.date = location_date[1]

        try:
            self.parsed_date = parser.parse(self.date)
        except:
            self.parsed_date = None

        self.description = get_description(self.soup)
        self.title = get_title(self.soup)

        self.coordinates = None


    def __repr__(self):
        return(f'Title: {self.title} | Location: {self.location} | ID: {self.id} | Date: {self.date}')

    def __str__(self):
        return(f'Title: {self.title} | Location: {self.location} | ID: {self.id} | Date: {self.date}')
