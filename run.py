import concurrent.futures
from post import Post
from get_ids import get_ids

def load_post(post_id):
    return Post(post_id)

post_ids = get_ids()

with concurrent.futures.ThreadPoolExecutor() as executor:
    posts = list(tqdm(executor.map(load_post, post_ids), total=len(post_ids)))

import datetime
import pandas as pd
today = datetime.datetime.today().strftime('%Y-%m-%d')

df = pd.DataFrame([(x.title, x.location, x.date, x.description, x.id, x.parsed_date) for x in posts])
df.columns = ['Title','Location','Date', 'Description', 'ID', 'Parsed Date']
df = df.sort_values(by=['Parsed Date', 'Location', 'Title'], ascending= [False, True, True])

df.to_csv(f'results_{today}.csv')

# Sorting by date
# posts = [x for x in posts if x.parsed_date != None]
# sorted(posts, key = lambda x: x.parsed_date)
