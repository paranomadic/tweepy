# For each twitter id (investor + VC), create an excel file with follower IDs.
	#Check for the new ones and stop if found
		# 1. load different xl files of all domains in twitter_names as a dataframe
		# 2. then check for the new user whether it belongs to the list already or not
		# 3. If not, add ot the list 
		# 4. Update the xl file

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
dftwitter = pandas.read_csv("twitter_names.csv")

for i in dftwitter["Names"]:
	os.chdir('Twitter/')

	try:
		dfusers = pandas.read_excel(i + '.xls', 'Startups')
	except:
		pass

	users = tweepy.Cursor(api.followers, screen_name= i, count=200).items()
	name = i
	print(i + '12345')
	#print(users)
	while True:
	    try:
	       user = next(users)
	       list1.append(user.screen_name) 
	       for j in list1:
	       		if j in dfusers[i]:
	       			continue
	       		else:
	       			list2.append(j)
	
	    except tweepy.TweepError:
	        time.sleep(60*16)
	        user = next(users)
	        list1.append(user.screen_name) 
	        for j in list1:
	       		if j in dfusers[i]:
	       			continue
	       		else:
	       			list2.append(j)
	        
	       # print(tweepy.TweepError)
	    except StopIteration:
	        break
	    #add new file creation, check the old followers and add only the ones in the list.
	    #list1.append(user.screen_name)
	    print(user.screen_name)

	df_new = pandas.DataFrame(list2)
	df_final = dfusers.append(df_new)
	outfile = i + ".xls"
	writer = ExcelWriter(outfile)
	df_final.to_excel(writer,'Startups',index=False, header = name)
	writer.save()
	list1=[]

#df_followers = pandas.DataFrame(list1)
#outfile = "Followertest.xls"
#writer = ExcelWriter(outfile)
#df_followers.to_excel(writer,'Startups',index=False)
#writer.save()

# For each twitter id, create a mechanism to check old followers and add only the ones not there in the list.