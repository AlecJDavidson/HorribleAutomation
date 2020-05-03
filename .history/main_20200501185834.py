### Parses RSS feed and adds desired magnet links to qbtorrent ###
### Author - Alec J. Davidson
### Imports ###
import feedparser # Allows the parsing of the RSS feeds
import sys # Imports the use of the system components
import os  # Imports the use of the file system
from qbittorrent import Client
root = os.getcwd()+'/' # Root directory of the project

def read_watch_list(): # Reads and creates usable list to iterate over
	watchListTxt = open(root+'watchlist.txt','r')
	watchList = []
	for entry in watchListTxt:
		watchList.append(entry.strip())
	return(watchList)

def rss_feed(): # Reads the RSS feed, parses it, stores the titles and links in respective lists
	rssList = [[],[]]
	feed = feedparser.parse('http://www.horriblesubs.info/rss.php?res=1080')
	i = 0
	while i < len(feed.entries):
		entry = feed.entries[i]
		rssList[0].append(entry.title)
		rssList[1].append(entry.link)
		i += 1
	return(rssList)

def link_list(): # Matches the watch list entries to the titles and links in the rss feed lists
	linkList = []
	i = 0
	for title in rss_feed()[0]:
		for entry in read_watch_list():
			if entry in title:
				linkList.append(rss_feed()[1][i])
		i += 1
	return(linkList)

def write_download_history(): # Writes downloaded magnet links to history.txt
	historyTxt = open(root+'history.txt','a')
	for link in link_list():
		historyTxt.write(link+'\n')

def qb_download(): ### Adds magnet links to qb ###
	qb = Client('http://127.0.0.1:8080/')
	qb.login('testing', 'testing')	# not required when 'Bypass from localhost' setting is active.
	historyTxt = open(root+'history.txt','r')
	historyList = []
	linkList = link_list()
	for links in historyTxt:
		historyList.append(links)
		linkList.remove(links.strip())
	for magnet_link in linkList:
		print(magnet_link)
		qb.download_from_link(magnet_link)
qb_download() # Calls qb_download function.
write_download_history()
