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

import time
import tweepy

# auth = tweepy.OAuthHandler('rP4vHHT0ccdmwFRKOcq9XNPpo', '3yPBdrP91MxLlIKHCY6IFCCq6BUoyETzI1pRzWsfRTDgcdPyTu')
# auth.set_access_token('765082989097136128-RAQ3H3L8OfM8D9qA5bbNMhRLU8Jb0Sr', 'NF9R6tZFHuXpRPkaGSGWGNAduiOP0vFeUpuvtDCNd61fx')

# api = tweepy.API(auth)

# ids = []
# for page in tweepy.Cursor(api.followers_ids, screen_name="Parandomadic").pages():
#     ids.extend(page)
#     time.sleep(60)

# print len(ids)
auth = tweepy.OAuthHandler('rP4vHHT0ccdmwFRKOcq9XNPpo', '3yPBdrP91MxLlIKHCY6IFCCq6BUoyETzI1pRzWsfRTDgcdPyTu')


try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

print(auth.access_token)
print(auth.access_token_secret)

verifier = raw_input('Verifier:')
