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
    for files in os.listdir(basepath):
        parsedFiles = PTN.parse(files)
        print(parsedFiles['title'])

def find_dir():
    if not os.path.exists('my_folder'):
    os.makedirs('my_folder')

tarDir = '/home/alec/Documents/Development/Python/TorrentDownloader/plex-media'
