import re
import requests
from bs4 import BeautifulSoup
from tools import make_alpha, make_numeric

def get_ids():
    base = 'https://groups.freecycle.org/group/WashingtonDC/posts/offer?page='
    urls = [base + str(i+1) for i in range(20)]
    # Request the pages
    pages = [requests.get(url) for url in urls]
    # Get the text from each page
    texts = [page.text for page in pages]
    # REGEX patterns for IDs
    pattern = re.compile('\(\#\d{1,10}\)')
    # Find the post ids
    ids = [re.findall(pattern,text) for text in texts]
    # Flatten the list
    ids = [item for sublist in ids for item in sublist]
    ids = [make_numeric(id) for id in ids]
    ids = list(set(ids))
    return ids
