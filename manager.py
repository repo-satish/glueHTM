import os, sys
from core_commandGenerator import main

cmdFile = "cmnds.bat"
cmnds = open(cmdFile, "wt", encoding="UTF-8")

cmnds.write("chcp 65001\n")
for _ in sys.argv:
	x = os.path.abspath(_).strip("\"")	# because path needs to be free from '"' & mixed '/' & '\'
	if os.path.isdir(x):
		cmnds.write(  main(x)  )
		cmnds.write("One fragment of job has completed.\n")
		cmnds.write("pause\n");		cmnds.write("explorer \"%(x)s\"" % locals());		cmnds.write("\n\n\n")
	else:	pass
# cmnds.write("chcp %(default)d\n" % locals()) not needed as OS restores the default codepage

cmnds.close()

"""
if 5-10 file in *_files/ its ok
move to recycle bin
analyse
	if binary heavy --> Normal.LZMA
	if text heavy --> Ultra.PPMd
"""