"""
	A tool to integrate .htm & its associated folders
	1. choose a dir from list of dirs having the form `*_files`
	2. if os.path.isfile(dir[:-6]): listOfFilesForThisArchive.append(dir[:-6])
	2. else just 7zip the dir & add prefix "HTM- incomplete- "
	3. make it
"""

import os, sys

parseLine = lambda line: line.replace("_files", "") if line.find("_files") != -1 else None

def main(path):
	program = "\"%programfiles%\\7-Zip\\7z\" "
	batchString = ""
	command = " a "
	switches = [" -y ", " -o "]
	
	listOfFiles = os.listdir(path)
	for x in listOfFiles:
		fileCompressList = list();
		archiveName = "\"" + path + "\\"
		pageName = parseLine(x)
		if pageName is None:	pass
		else:
			cName = path+"\\"+pageName
			if ( pageName+".htm" ) in listOfFiles:		fileCompressList.append(" \""+cName+".htm"+"\" ")
			elif ( pageName+".html" ) in listOfFiles:	fileCompressList.append(" \""+cName+".html"+"\" ")
			else:									archiveName+= "(incomplete)"
			fileCompressList.append(" \""+cName+"_files\" ")
			archiveName+= "HTM- "
			archiveName+= pageName+".7z\" "
			batchString+= program + command + archiveName + (''.join(fileCompressList)) +"\n"
			batchString+= "del /q \""+cName+".h*\" " +"\n"
			batchString+= "rd /s /q \""+cName+"_files\" " +"\n"
			del fileCompressList, archiveName
	return batchString


# TODO: automate batch file creation & running
