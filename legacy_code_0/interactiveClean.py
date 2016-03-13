"""
traverses through the dirs and files in given root and ask following questions sequentially:
	- tells if file is complete or incomplete
	- compression method selection [zip.Store]
	- want to compress [y]
	- do u want to rename it (if compression was successful) [None for COMPLETEs & prepend with 'incomplete-- ' for INCOMPLETEs]
	- do u want to delete the old files (if archive is error free) [y]
"""
