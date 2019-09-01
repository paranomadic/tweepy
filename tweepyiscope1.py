#CREATING DATABASE OF ALL THE TWITTER FOLLOWERS
#==============================================

import tweepy
import time
import pandas
from pandas import ExcelWriter
import os
import glob

ACCESS_TOKEN = '**************************'
ACCESS_SECRET = '***********************'
CONSUMER_KEY = '*************************'
CONSUMER_SECRET = '************************'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

list1 = []
list2 = []
count = 0

dftwitter = pandas.read_csv("twitter_names.csv")
os.chdir('Twitter/')
filelist = glob.glob("*.xls")
print(filelist)

for i in dftwitter["Names"]:
	print(i)
	name = i
#Check if file of that handle is present or not
	if name in filelist:
		continue
	else:
		datafile = pandas.DataFrame(list2,index = None,columns = ['@Handle'])
		outfile = i + ".xls"
		writer = ExcelWriter(outfile)
  		datafile.to_excel(writer,i,index=False)
  		writer.save()
#Extract all followers and put them in the file
	users = tweepy.Cursor(api.followers, screen_name = i, count=200).items()

	while True:
		try:
			user = next(users)
			count = count + 1
			list1.append(user.screen_name)
			print(count)
		except tweepy.TweepError:
			time.sleep(60*16)
			user = next(users)
			count = count + 1
			list1.append(user.screen_name)
			print(count)
		except StopIteration:
			break

	#Add new files with first heading as the tweet handle
	list2 = [i]*count
	df_final = pandas.DataFrame(list1,index = None,columns = ['@Handle'])
	outfile = i + '.xls'
	writer = ExcelWriter(outfile)
	#Change twitter file second column when a file is created (end of the loop)
	df_final.to_excel(writer,'Startups', index = None, columns = ['@Handle'])
	writer.save()
	list1=[]
	count = 0

	


	










