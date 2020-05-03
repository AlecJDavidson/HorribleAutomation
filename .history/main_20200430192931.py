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

# ### Setting up qb ###
# qb = Client('http://127.0.0.1:8080/')
# qb.login('testing', 'testing')	# not required when 'Bypass from localhost' setting is active.

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
	
def rssFeed():
	rssList = [[],[]]
	feed = feedparser.parse(horribleSubsRSS)
	i = 0
	while i < len(feed.entries):
		entry = feed.entries[i]
		rssList[0].append(entry.title)
		rssList[1].append(entry.link)
		i += 1
	return(rssList)
i = 0
while i < len(rssFeed()[0]):
	print(rssFeed()[0][i])
	i += 1

# # ### Adds magnet links to qb ###
# for magnet_link in findMatch():
# 	print(magnet_link)
# 	qb.download_from_link(magnet_link)


