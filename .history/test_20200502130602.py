### Moves my downloads automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import os  # Imports the use of the file system
import shutil # Allows me to move files.
import PTN # Parses the torrent name.
root = os.getcwd()+'/' # Root directory of the project

# List all files in a directory using os.listdir

def get_files(): # Creates a usable list of files in the completed downloads folder
	downDir = os.listdir(root+'Downloads')
	downFiles = []
	for files in downDir:
		downFiles.append(files)
	return (downFiles)

def parse_files(): # Stores the raw titles in [0] and the parsed titles in [1].
	parsedTitles = get_files()
	titleList = [[],[]]
	for title in parsedTitles:
		titleList[0].append(title)
		titleList[1].append((PTN.parse(title)['title'])[:-4])
	return(titleList)

# def get_dir(): # Uses the file names to find directories of the same name. If one is not found it will be created.


def create_dir(): # Creates a directory if one does not already exist for it's respective title.
	animeDir = os.listdir(root+'plex-media/anime')
	titleDirs = []
	# for title in parse_files()[1]:
	# 		if not os.path.exists(title):
	# 			os.makedirs(title)
	
create_dir()



# def move_files(): # Moves the files one by one to the directories with matching names.