# Consumer Key (API Key)	rP4vHHT0ccdmwFRKOcq9XNPpo
# Consumer Secret (API Secret)	3yPBdrP91MxLlIKHCY6IFCCq6BUoyETzI1pRzWsfRTDgcdPyTu
# Access Level	Read and write (modify app permissions)
# Owner	Paranomadic
# Owner ID	765082989097136128
# 	Access Token	765082989097136128-RAQ3H3L8OfM8D9qA5bbNMhRLU8Jb0Sr
# Access Token Secret	NF9R6tZFHuXpRPkaGSGWGNAduiOP0vFeUpuvtDCNd61fx
# Access Level	Read and write
# Owner	Paranomadic
# Owner ID	765082989097136128

# import time
# import tweepy

# auth = tweepy.OAuthHandler('rP4vHHT0ccdmwFRKOcq9XNPpo', '3yPBdrP91MxLlIKHCY6IFCCq6BUoyETzI1pRzWsfRTDgcdPyTu')
# auth.set_access_token('765082989097136128-RAQ3H3L8OfM8D9qA5bbNMhRLU8Jb0Sr', 'NF9R6tZFHuXpRPkaGSGWGNAduiOP0vFeUpuvtDCNd61fx')

# api = tweepy.API(auth)

# ids = []
# for page in tweepy.Cursor(api.followers_ids, screen_name="Parandomadic").pages():
#     ids.extend(page)
#     time.sleep(60)

# print len(ids)
try:
    import json
except ImportError:
    import simplejson as json
import twitter
import requests

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = '765082989097136128-RAQ3H3L8OfM8D9qA5bbNMhRLU8Jb0Sr'
ACCESS_SECRET = 'NF9R6tZFHuXpRPkaGSGWGNAduiOP0vFeUpuvtDCNd61fx'
CONSUMER_KEY = 'rP4vHHT0ccdmwFRKOcq9XNPpo'
CONSUMER_SECRET = '3yPBdrP91MxLlIKHCY6IFCCq6BUoyETzI1pRzWsfRTDgcdPyTu'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=Paranomadic&count=5000'

results = requests.get(url)

better_results = results.json()

print(better_results)































