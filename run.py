import concurrent.futures
from post import Post
from get_ids import get_ids

def load_post(post_id):
    return Post(post_id)

post_ids = get_ids()

with concurrent.futures.ThreadPoolExecutor() as executor:
    posts = list(executor.map(load_post, post_ids))

# Sorting by date
posts = [x for x in posts if x.parsed_date != None]
sorted(posts, key = lambda x: x.parsed_date)
