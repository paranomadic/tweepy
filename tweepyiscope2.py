#RENEWING THE DATABASE OF ALL THE TWITTER FOLLOWERS
#==============================================

import tweepy
import time
import pandas
from pandas import ExcelWriter
import os

ACCESS_TOKEN = '765082989097136128-RAQ3H3L8OfM8D9qA5bbNMhRLU8Jb0Sr'
ACCESS_SECRET = 'NF9R6tZFHuXpRPkaGSGWGNAduiOP0vFeUpuvtDCNd61fx'
CONSUMER_KEY = 'rP4vHHT0ccdmwFRKOcq9XNPpo'
CONSUMER_SECRET = '3yPBdrP91MxLlIKHCY6IFCCq6BUoyETzI1pRzWsfRTDgcdPyTu'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

list1 = []
list2 = []
count = 0
dftwitter = pandas.read_csv("twitter_names.csv")
os.chdir('Twitter/')

for i in dftwitter["Names"]:
	
	name = i + '.xls'
	print(name)

	try:
		dfusers = pandas.read_excel(name, 'Startups',index=True)
		print(dfusers['@Handle'])
	except:
		pass

	for j in dfusers['@Handle']:
		list1.append(j)

	users = tweepy.Cursor(api.followers, screen_name = i, count=200).items()

	while True:
		try:
			user = next(users)
			if user.screen_name in list1:
				print(111)
			else:
				list2.append(user.screen_name)
				print(222)
		
		except tweepy.TweepError:
			time.sleep(60*16)
			user = next(users)
			if user.screen_name in list1:
				print(111)
			else:
				list2.append(user.screen_name)
				print(222)
		except StopIteration:
			break

	#Combine new and old names in a single sheet

	df_final = pandas.DataFrame(list2)
	dfinal = pandas.concat([dfusers,df_final],axis=0)
	outfile = i + ".xls"
	writer = ExcelWriter(outfile)
	dfinal.to_excel(writer,'Startups', header = i,index = True)
	writer.save()
	list1=[]
	list2=[]

