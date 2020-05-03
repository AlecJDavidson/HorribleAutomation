### Downloads my torrents automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import time # Allows the use of scheduled arguments
import sys # Imports the use of the system components
import os  # Imports the use of the file system
import shutil # Allows me to move files.
root = os.getcwd()+'/' # Root directory of the project

# List all files in a directory using os.listdir
def downloads():
    basepath = '/home/alec/Downloads'
    for files in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, files)):
            return (files)


print(downloads()[1])