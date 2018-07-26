import requests
from bs4 import BeautifulSoup

#Generate the URLs
base = 'https://groups.freecycle.org/group/WashingtonDC/posts/all?page='
urls = [base + str(i+1) for i in range(20)]

# Request the pages and parse
pages = [requests.get(url) for url in urls]
soups = [BeautifulSoup(page.text, 'html.parser') for page in pages]

bad_elements = [' > OFFER ','See details', ' • WANTED '] # Remove these text fields

text_list = []
for soup in soups:
    table = soup.find('table', id="group_posts_table")
    try:
        texts = table.findAll('a')
    except:
        pass
    items = [text.text for text in texts if text.text not in bad_elements]
    text_list.extend(items)

clean_items = list(set(text_list)) # Remove duplicates
clean_items = [x.strip() for x in clean]

for item in clean:
    print(item)
