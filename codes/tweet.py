#!/usr/bin/python2
import time
from twython import TwythonStreamer, Twython , TwythonError


#Twitter app auth
APP_KEY = '<>'
APP_SECRET = '<>'
OAUTH_TOKEN = '<>'
OAUTH_TOKEN_SECRET = ''

#sleep time between checks to avoid RT rate limits
sleeptime = 5000
#Let's gather a list of words we DON'T want to RT
naughty_words = ["CPU", "TEMP", "courses", "hiring", "load average", "Temperature and humidity sensor", "Comunidade"]
#And a list of words we WOULD like to RT

good_words = ["#linux", "TheTunnelix", "#Debian", "#mauritius", "#pentesting" , "#infotech", "#hacking", "linkbynet" , "#vulnerabilities" , "#raspberrypi", "hackers.mu", "#Kalilinux", "internet.org" , "HNTweets", "#torproject" , "#infosec" , "#SysAdmin" ]

#OR is Twitter's search operator to search for this OR that
#So let's join everything in good_words with an OR!
filter = " OR ".join(good_words)

# The - is Twitter's search operator for negative keywords
# So we want to prefix every negative keyword with a -
blacklist = " -".join(naughty_words)

#And finally our list of keywords that we want to search for
#This will search for any words in good_words minus any naughty_words
keywords = filter #+ blacklist
#Setting Twitter's search results as a variable
while (True):
	try:
		twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		search_results = twitter.search(q=keywords, count=1)
	#time.sleep(600)	
		for tweet in search_results["statuses"]:
			print tweet
			try:
				twitter.retweet(id = tweet["id_str"])
			except TwythonError as e:
				print e
		time.sleep(sleeptime)
	except TwythonError as e:
		print e
