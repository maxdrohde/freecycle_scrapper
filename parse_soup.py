# Functions to parse BS4 objects from FreeCycle post pages

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
