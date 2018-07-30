# Functions to parse BS4 objects from FreeCycle post pages
from tools import sanatize

def get_location_and_date(soup):
    detail = soup.find('div', id="post_details")
    if detail == None:
        return 'No location / date'
    try:
        children = [x.text for x in detail.children if len(str(x)) > 3]
        location = children[0].split(':')[1].strip()
        date = children[1].split(':',1)[1].strip()
    except:
        return 'No location', 'No date'

    return sanatize(location), date

def get_description(soup):
    detail = soup.find('div', id="group_post")
    if detail == None:
        return 'No description'
    desc = detail.find('p').text.strip()
    return sanatize(desc)

def get_title(soup):
    headers  = soup.findAll('header')
    if headers == None:
        return 'No title'
    try:
        title = [x.text for x in headers if 'OFFER' in x.text][0]
        title = title.split('OFFER:')[1].strip()
    except:
        return('No title')
    return sanatize(title)
