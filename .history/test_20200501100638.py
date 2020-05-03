### Downloads my torrents automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import time # Allows the use of scheduled arguments
import sys # Imports the use of the system components
import os  # Imports the use of the file system
import shutil # Allows me to move files.
import PTN # Parses the torrent name.
root = os.getcwd()+'/' # Root directory of the project

# List all files in a directory using os.listdir
def list_downloads():
    basepath = '/home/alec/Documents/Development/Python/TorrentDownloader/Downloads'
    parsedList = []
    for files in os.listdir(basepath):
        parsedList.append(PTN.parse(files)['title'])
    return (parsedList)

def find_dir():
    path = '/home/alec/Documents/Development/Python/TorrentDownloader/plex-media/anime'

    for files in list_downloads():
        if not os.path.exists(str(path+files)):
            print('creating dir')

            os.makedirs(path+files)
        else:
            print('dir exists write code to move files')
find_dir()

tarDir = '/home/alec/Documents/Development/Python/TorrentDownloader/plex-media'
