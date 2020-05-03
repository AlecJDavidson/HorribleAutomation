### Downloads my torrents automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import re # Helps with searching lists
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

root = os.getcwd()+'/' # Root directory of the project

### RSS Feeds go here ###
horribleSubsRSS = 'http://www.horriblesubs.info/rss.php?res=1080'

##################################

### Watch List ###
def watchList():
    watchlist = open(root+'watchlist.txt','r') # Opens watchlist to read
    watchlistList = [] # Creates a list file in python to hold entries
    for watchlistEntry in watchlist: # Iterates over watch list to add new entries
        # print(watchlistEntry)
        watchlistList.append(watchlistEntry.strip()) # Adds new entries
        watchlistList = list(dict.fromkeys(watchlistList)) # Converts to dictionary to remove duplicates
    return(watchlistList)
# print('printing watch list:')
# for i in watchList():
#     print(i)
    
##################################

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

##################################

### Update RSS list ###
def rssList():
    rssList = [] # Creates a list to store the entries
    feed = feedparser.parse(horribleSubsRSS)
    # print ('Number of RSS posts :', len(feed.entries))
    i = 0
    while i < len(feed.entries):
        entry = feed.entries[i]
        # print ('Title :',entry.title)
        # print ('Magnet Link :',entry.link)
        i = i + 1
    return(rssList)
# print('printing RSS list:')
# for i in rssList():
#     print(i)

##################################
