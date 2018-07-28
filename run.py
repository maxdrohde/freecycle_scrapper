from post import Post
from get_ids import get_ids
from tools import sanatize
from geopy.geocoders import Nominatim

print ('###########################')
print ('#### Starting scraping ####')
print ('###########################')
print()

# Load the IDs
ids = get_ids()
print(f'There are {len(ids)} ids')
print()

# Load the posts
post_list = []
for i, x in enumerate(ids):
    if i % 5 == 0:
        print(f'Processing post number {i} of {len(ids)}')
    try:
        post_list.append(Post(x))
    except:
        print(f'An error occured in post {i}')
    print('COMPLETED')

locations = [sanatize(post.location) for post in post_list]

geolocator = Nominatim(user_agent="my-application")

# Get coordinates of posts
coords = []
for location in locations:
    geo_loc = geolocator.geocode(location)
    try:
        coord = (geo_loc.latitude, geo_loc.longitude)
        print(coord)
        coords.append(coord)
    except:
        print(repr(location))

good_locations = ['brookland', 'noma', 'ne', 'silver spring']
good_posts = [post for post in post_list if 'brookland' in sanatize(post.location)]
