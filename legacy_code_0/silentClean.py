import os, sys
import zipfile
import datetime

partB4ext = lambda x: os.path.splitext(x)[0]


def do(archiveHandle, target):
	def getCtime(x):
		ans = os.stat(os.path.abspath(x))[9]
		ans = datetime.datetime.fromtimestamp(  ans  ).strftime('%Y_%m_%d_%H_%M_%S').split('_')
		for i, value in enumerate(ans):
			ans[i] = int(value)
		return tuple(ans)
	op = os.path
	target = op.abspath(target)
	for currRoot, dirs, files in os.walk(target):
		for aFile in files:
			p1 = op.abspath(aFile)
			p2 = p1[len(    op.commonpath([p1, target])    )+1:]
			# p1, p2 = p1.encode("UTF-8"), p2.encode("UTF-8")
			# archiveHandle.write(p1, arcname=p2)
			print(p1)
			print(p2)
			input()
		for aDir in dirs:
			x = op.abspath(aDir)
			relPath = x[len(    op.commonpath([x, target])    )+1:]+os.sep
			zipInfo = zipfile.ZipInfo(relPath, getCtime(aDir))	# TODO-- implement os.stat().st_mode -> zipfile.external_attr in future versions
			# archiveHandle.writestr(zipInfo, '')
			print(relPath)
			input()
		"""
		strange behaviour is seen here, for some reason instead of going deeper into the target dir, control flows towards root.
		to replicate unzip code.7z and cd into -sandbox dir and run only this function
			- problem in os.walk
			- try os.walk(top, topDown=True)
			- try os.scandir
			- maybe there is a problem with the statements using commonpath thingy, implement own algorithm
		its time to branch off, use 7z executable and make system calls, let this dependency free version
		sit idle till this issue is resolved.
		If everything fails, see last portion on 'research_on_zipfile_module.py' of `pysanezip module`
		"""
	return

def archive(dirName, fileName, deleteOnSuccess, outputFileName):
	# out of concern of performance of the next 3 lines, see DEBUG0.py
	with zipfile.ZipFile(outputFileName, mode='a', compression=zipfile.ZIP_STORED) as zfh:
		do(zfh, dirName)
		zfh.write(fileName, os.path.basename(fileName))
	if deleteOnSuccess and os.path.isfile(outputFileName):
		with zipfile.ZipFile(outputFileName, mode='r') as x:
			if x.testzip() not None:
				print("Zipped archive file is corrupted, re-attempting sanitization")
				archive(dirName, fileName, deleteOnSuccess, outputFileName)
		subprocess.call("del %(BLANK)s" % locals(), shell=True)
	return

def listWebpages(locn):
	locn = os.path.abspath(locn)
	webpages = dict(zip(["complete", "singleton", "incomplete"], [None]*3))
	for root, dirs, files in os.walk(locn):	# os.listdir not reliable
		if root is locn:
			break
	files = [partB4ext(_) for _ in files if ".htm" in os.path.splitext(_)[1]]
	dirs = [_[:-6] for _ in dirs if _.endswith("_files")]	# endswith will work because dir names do not end with '\\' or '/' in values returened by os.walk
	webpages["complete"] = [_ for _ in files if os.path.isdir(_+"_files")]
	webpages["incomplete"]=[_ for _ in dirs if not os.path.isfile(_+".htm") and not os.path.isfile(_+".html")]
	# ? the following line is just show off, not really needed
	webpages["singleton"]= list(set(files).difference(  set(webpages["complete"])  ))	# [_ for _ in files if not os.path.isdir(_+"_files")]
	return webpages

def clean(locn, deleteOld):
	kya = True if deleteOld else False
	webpages = listWebpages(locn)
	print("--Processing complete webpages--")
	for x in webpages["complete"]:
		x = os.path.join(os.path.abspath(locn), x)
		y = os.path.basename(x)
		if os.path.isfile(x+".htm"):
			fullName = x+".htm"
		elif os.path.isfile(x+".html"):
			fullName = x+".html"
		else:
			input("Someone butched the directory while I was processing it :(")
			sys.exit(0)
		archive(
			dirName=x+"_files",
			fileName=fullName,
			deleteOnSuccess=kya,
			outputFileName=y+".htmz"
		)
	print("--Processing incomplete webpages--")
	for x in webpages["incomplete"]:
		y = os.path.basename(x)
		archive(
			dirName=x+"_files",
			fileName=None,
			deleteOnSuccess=kya,
			outputFileName="incomplete-- "+y+".htmz"
		)
	return

def main(locn):
	clean(locn, deleteOld=True)
	return


if __name__ == '__main__':
	main(locn)
