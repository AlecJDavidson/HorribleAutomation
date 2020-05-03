### Moves my downloads automatically ###
### Author - Alec J. Davidson
### Version .01

### Imports ###
import os  # Imports the use of the file system
import shutil # Allows me to move files.
import PTN # Parses the torrent name.
root = os.getcwd()+'/' # Root directory of the project

downDir = os.listdir(root+'Downloads') # Where the torrents are downloaded.
animeDir = (root+'plex-media/anime/') # Path to anime folder

def get_files(): # Creates a usable list of files in the completed downloads folder
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

def create_dir(): # Creates a directory if one does not already exist for it's respective title.
	for title in parse_files()[1]:
			if not os.path.exists(animeDir+title):
				os.makedirs(animeDir+title)
create_dir()

print(parse_files()[0])



# def move_files(): # Moves the files one by one to the directories with matching names.