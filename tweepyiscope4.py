#AFTER tweepyiscope3.py, run a pivot (presently on excel) around all followers to get a count of the most common followers.
# Store the list in an excel and write a program that fetches all info about the tweet handles of these followers.

import tweepy
import time
import pandas
from pandas import ExcelWriter
import os

ACCESS_TOKEN = '**************************'
ACCESS_SECRET = '***********************'
CONSUMER_KEY = '*************************'
CONSUMER_SECRET = '************************'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

os.chdir('Twitter/')
df_followers_hot = pandas.read_csv("selection.csv")

list1 = []
list2 = []
cols = ['Twitter Handle','Description','url']

for i in df_followers_hot["Twitter Handle"]:
	data = api.get_user(i)
	#print(data.description)
	#print(data.url)
	desc = data.description
	list1.append(desc)

	url = data.url
	list2.append(url)

df_followers_hot.ix[:,"Description"] = list1
df_followers_hot.ix[:,"url"] = list2

os.chdir('Final/')
outfile = 'selected'+'.xls'
writer = ExcelWriter(outfile)
df_followers_hot.to_excel(writer,'Details',index=False)
writer.save()
