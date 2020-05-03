### Downloads my torrents automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import time # Allows the use of scheduled arguments
import feedparser # Allows the parsing of the RSS feeds
import urllib.request # Allows that download and storage of files
import bs4 # Allows web scraping
import sys # Imports the use of the system components
import os  # Imports the use of the file system
from qbittorrent import Client
##################################

### Setting up qb ###
qb = Client('http://127.0.0.1:8080/')
qb.login('testing', 'testing')
# not required when 'Bypass from localhost' setting is active.
# defaults to admin:admin.
# to use defaults, just do qb.login()
##################################

### RSS Feeds go here ###
horribleSubsRSS = 'http://www.horriblesubs.info/rss.php?res=1080'
##################################

### List of Anime to watch for ###
root = os.getcwd()+'/' # Root of the project
watchlist = open(root+'watchlist.txt','r') # Opens watchlist to read
watchlistList = [] # Creates a list file in python to hold entries
print('Printing current watch list')
for watchlistEntry in watchlist: # Iterates over watch list to add new entries
    print(watchlistEntry)
    watchlistList.append(watchlistEntry) # Adds new entries
    watchlistList = list(dict.fromkeys(watchlistList)) # Converts to dictionary to remove duplicates
    print(watchlistList)
##################################

### List of episodes that have been downloaded to prevent redownload ###
historylist = open(root+'history.txt','r') # Opens download history
historylistList = [] # Creates a list file in pythone to hold entries
print('Printing download history')
for historylistEntry in historylist: # Iterates over download history
    print(historylistEntry)
    historylistList.append(historylistEntry) # Adds new entries
    historylistList = list(dict.fromkeys(historylistList))
    print(historylistList)

### Check for new episodes ###
feed = feedparser.parse(horribleSubsRSS)
print ('Number of RSS posts :', len(feed.entries))
i = 0
while i < len(feed.entries):
    entry = feed.entries[i]
    print (entry.title)
    # print ('Magnet Link :',entry.link)
    i = i + 1
else:
    print('End of RSS Feed')

##################################

def createDownloadList(): # Filters lists so there are no repeat downloads
    link_list = [] # Creates link list
    print(watchlistEntry)
    if watchlistEntry in entry.title:
        print('True')
    else:
        print('False')

createDownloadList()



