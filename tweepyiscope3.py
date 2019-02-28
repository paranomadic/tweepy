#AGGREGATE LIST OF ALL TWITTER FOLLOWERS
#=======================================================

import tweepy
import time
import pandas
from pandas import ExcelWriter
import os
import glob
import re
import numpy

os.chdir('Twitter/')
filelist = glob.glob("*.xls")
count = 0
list1 = []

# 1. Putting every follower in a single document. Table with two columns. 1st: screen_name 2nd: The one whom they are following.

for filename in filelist:
	df = pandas.read_excel(filename)
	list1.append(df)
	number = len(list1)
	print(number)
	count = count + 1
	print(count)

concated_df = pandas.concat(list1, axis = 0)
concated_df.to_csv('all.csv', index=None)

#p = concated_df.pivot_table(index='@Handle', aggfunc = len,fill_value=0)
#p.to_csv('all.csv', index=None)