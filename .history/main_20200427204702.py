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
qb.login('testing', 'testing')
# not required when 'Bypass from localhost' setting is active.
# defaults to admin:admin.
# to use defaults, just do qb.login()
##################################

### List of Anime to watch for ###
root = os.getcwd()+'/' # Root of the project
watchlist = open(root+'watchlist.txt') # Opens watchlist to read
print('Printing current watch list')
print(watchlist.read())
##################################

### List of episodes that have been downloaded to prevent redownload ###
#history = open(root+)

### RSS Feeds go here ###
horribleSubsRSS = 'http://www.horriblesubs.info/rss.php?res=1080'
##################################

### Testing

feed = feedparser.parse(horribleSubsRSS)

print ('Number of RSS posts :', len(feed.entries))

i = 0
while i < len(feed.entries):
    entry = feed.entries[i]
    print ('Title :',entry.title)
    print ('Magnet Link :',entry.link)
    i = i + 1
else:
    print('End of RSS Feed')
