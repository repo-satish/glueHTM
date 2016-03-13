"""
	merges `_files/` and `.htm(l)` into a nice zip file
"""

import os, sys
import zipfile

def zipEm(pageNames, incompletes):					# doing nothing about singleList
	
	pass

def func1(dirList, fileList):						# commonize
	pageNameList, singleList, incompletes = list(), list(), list()
	for _ in dirList:
		if _[-6:] is "_files":				pageNameList.append(_)
		else:								pass
	for _ in pageNameList:							# search in fileList, if not found -- MOVE to incomplete[] else POP
		if _+".htm" in fileList:				fileList.remove(_+".htm")
		elif _+".html" in fileList:				fileList.remove(_+".html")
		else:
			pageNameList.remove(_)
			incompletes.append(_)
	for _ in fileList:								# ? check fileList for .htm and .htmls
		if _.find(".htm") == -1:
			singleList.append(_)
	# if len(dirs) > len(files):--NEWLINE--		for index, entry in enumerate(files):						# traverse the shorter list--NEWLINE--			if entry[-4:] is ".htm" or entry[-5:] is ".html":--NEWLINE--				pageNames.append(entry)--NEWLINE--				what = "dirs"--NEWLINE--				dirs.remove(entry[entry.rfind("."):]+"_files")--NEWLINE--	else:									# lengths equal or--NEWLINE--		for index, entry in enumerate(dirs):--NEWLINE--			if entry[-6:] is "_files":--NEWLINE--				what = "files"--NEWLINE--				try: files.remove(entry[entry.rfind("_files"):]+".htm")--NEWLINE--				except: files.remove(entry[entry.rfind("_files"):]+".html")--NEWLINE--				else: incompletes.append(entry)--NEWLINE--				pageNames.append(entry)--NEWLINE--	# treat those -- folder is there, .htm nt there && pure .htm
	pass

def func0(path):
	if os.path.isabs(path):					pass
	else:									path = os.path.abspath(path)
	if os.path.isdir(path):					pass
	else:		return "\n%(path)s is not a directory\n--------------------------\n" % locals()
	for root, dirs, files in os.walk(path, topdown=True, onerror=None, followlinks=False):
		if root is ".":			break				# else:	pass, not needed cz only 1 iteration is needed
	func1(dirs, files)
	pass

def main():
	try:
		sys.argv[1]
	except IndexError:
		print(helpText)
	else:
		with open("cleaner.cmd", mode="wt", encoding="UTF-8") as f:
			for i in range(1, len(sys.argv)):
				f.write(    func0(sys.argv[i])    )	# !!!--- see codeBlock before `os.fwalk` in Python 3.5 docs
		input("processing complete, run cleaner.cmd")

if __name__ == '__main__':
	main()