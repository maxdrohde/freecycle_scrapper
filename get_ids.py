import re
import requests
from bs4 import BeautifulSoup
from tools import make_alpha, make_numeric, flatten
import concurrent.futures

def generate_urls():
    base = 'https://groups.freecycle.org/group/WashingtonDC/posts/offer?page='
    urls = [base + str(i+1) for i in range(50)]
    return urls

def get_ids_from_url(url):
    page = requests.get(url)
    text = page.text
    pattern = re.compile('\(\#\d{1,10}\)')
    page_ids = re.findall(pattern,text)
    page_ids = [make_numeric(id) for id in page_ids]
    return page_ids

def get_ids():
    urls = generate_urls()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        post_ids = list(executor.map(get_ids_from_url, urls))
    post_ids = list(flatten(post_ids))
    return post_ids
