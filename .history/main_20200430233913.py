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

root = os.getcwd()+'/' # Root directory of the project

### RSS Feeds go here ###
horribleSubsRSS = 'http://www.horriblesubs.info/rss.php?res=1080'

### Watch List ###
def watch_list():
	watchlist = open(root+'watchlist.txt','r') # Opens watchlist to read
	watchlistList = [] # Creates a list file in python to hold entries
	for watchlistEntry in watchlist: # Iterates over watch list to add new entries
		watchlistList.append(watchlistEntry.strip()) # Adds new entries
		watchlistList = list(dict.fromkeys(watchlistList)) # Converts to dictionary to remove duplicates
	return(watchlistList)
	

def rss_feed():
	rssList = [[],[]]
	feed = feedparser.parse(horribleSubsRSS)
	i = 0
	while i < len(feed.entries):
		entry = feed.entries[i]
		rssList[0].append(entry.title)
		rssList[1].append(entry.link)
		i += 1
	return(rssList)

def filter_match():
	linkList = []
	i = 0
	for title in rss_feed()[0]:
		for entry in watch_list():
			if entry in title:
				# print(title,rss_feed()[1][i])
				linkList.append(rss_feed()[1][i])
		i += 1
	return(linkList)

def write_download_history():
	downloadlist = open(root+'history.txt', 'a')
	for link in filter_match():
		print(link)
		downloadlist.write(link+'\n')
	return(downloadlist)

print(write_download_history())

# def download_filter():
#     history = open(root+'history.txt','r') # Opens history to read
#     historyList = []
#     magnetLinks = filter_match()
#     for links in history:
#         historyList.append(links.strip('\n'))
#     for savedLink in (historyList):
#         if savedLink in filter_match():
#             print('Link not added')
#     return(magnetLinks)
# for i in download_filter():
#     print(i)



# def qb_download(): ### Adds magnet links to qb ###
#     qb = Client('http://127.0.0.1:8080/')
#     qb.login('testing', 'testing')	# not required when 'Bypass from localhost' setting is active.
#     for magnet_link in filter_match():
#         print(magnet_link)
# 		for i in 
#         qb.download_from_link(magnet_link)
# qb_download()
