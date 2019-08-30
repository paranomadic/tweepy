# -*- coding: utf-8 -*-
import tweepy
import time
import pandas
from pandas import ExcelWriter

ACCESS_TOKEN = '**************************'
ACCESS_SECRET = '***********************'
CONSUMER_KEY = '*************************'
CONSUMER_SECRET = '************************'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

list1 = []

dftwitter = pandas.read_csv("twitter_names.csv")

# for i in dftwitter["Names"]:
users = tweepy.Cursor(api.friends, screen_name='ianetwork', count=200).items()
# print('1234'+i)
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
    	time.sleep(60*16)
    	user = next(users)
    except StopIteration:
        break
    list1.append(user.screen_name)
    print(user.screen_name)

df_followers = pandas.DataFrame(list1)
outfile = "Friendtest.xls"
writer = ExcelWriter(outfile)
df_followers.to_excel(writer,'usernames',index=False)
writer.save()
