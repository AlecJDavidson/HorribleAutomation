### Downloads my torrents automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import time # Allows the use of scheduled arguments
import feedparser # Allows the parsing of the RSS feeds
import urllib.request # Allows that download and storage of files
import sys # Imports the use of the system components
import os  # Imports the use of the file system
from qbittorrent import Client

### Setting up qb ###
qb = Client('http://127.0.0.1:8080/')
qb.login('testing', 'testing')	# not required when 'Bypass from localhost' setting is active.

root = os.getcwd()+'/' # Root directory of the project

### RSS Feeds go here ###
horribleSubsRSS = 'http://www.horriblesubs.info/rss.php?res=1080'

### Watch List ###
def watchList():
	watchlist = open(root+'watchlist.txt','r') # Opens watchlist to read
	watchlistList = [] # Creates a list file in python to hold entries
	for watchlistEntry in watchlist: # Iterates over watch list to add new entries
		watchlistList.append(watchlistEntry.strip()) # Adds new entries
		watchlistList = list(dict.fromkeys(watchlistList)) # Converts to dictionary to remove duplicates
	return(watchlistList)
# print('printing watch list:\n')
# for i in watchList():
#     print(i)

### Download List ###
def downloadList():
	downloadlist = open(root+'history.txt','r') # Opens download history
	downloadlistList = [] # Creates a list file in pythone to hold entries
	for downloadlistEntry in downloadlist: # Iterates over download download
		# print(downloadlistEntry)
		downloadlistList.append(downloadlistEntry.strip()) # Adds new entries
		downloadlistList = list(dict.fromkeys(downloadlistList))
	return(downloadlistList)
# print('printing download list:')
# for i in downloadList():
#     print(i)
	
def rssFeed():
	rssList = []
	feed = feedparser.parse(horribleSubsRSS)
	i = 0
	while i < len(feed.entries):
		entry = feed.entries[i]
		rssList.append(entry.title+entry.link)
		i += 1
	return(rssList)
# for i in rssFeed():
# 	print(i,'\n')

def findMatch():
	titles = []
	magnetLinks = []
	watchEntries = []
	for i in watchList():
		watchEntries.append(i)
	rssEntries = []
	for i in rssFeed():
		rssEntries.append(i)

	matchList = []
	i = 0
	while i < len(watchEntries):
		res = list(filter(lambda x: watchEntries[i] in x, rssEntries)) 
		print(res)
	# 	match = (str(res).split('.mkv'))
	# 	matchList.append(match)
		i += 1
	# for i in matchList:
	# 	magnetLinks.append(i[1])
	# 	titles.append(i[0])
	# return (magnetLinks)

### Adds magnet links to qb ###
for magnet_link in findMatch():
	qb.download_from_link(magnet_link)

