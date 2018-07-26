import requests
from bs4 import BeautifulSoup

base = 'https://groups.freecycle.org/group/WashingtonDC/posts/all?page='
urls = [base + str(i+1) for i in range(20)]

pages = [requests.get(url) for url in urls]

soups = [BeautifulSoup(page.text, 'html.parser') for page in pages]

text_list = []
for soup in soups:
    table = soup.find('table', id="group_posts_table")
    try:
        texts = table.findAll('a')
    except:
        pass
    bads = [' > OFFER ','See details', ' • WANTED ']
    lis = [text.text for text in texts if text.text not in bads]
    text_list.extend(lis)

clean = list(set(text_list))
clean = [x.strip() for x in clean]

for item in clean:
    print(item)
