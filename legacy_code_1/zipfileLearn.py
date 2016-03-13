"""
	zipfile library usage trials
"""

import os, zipfile


with zipfile.ZipFile("archiveName.zip", "w", compression=zipfile.ZIP_STORED) as zipFileHandle:

	for root, dirs, files in os.walk(os.getcwd()):
		zipFileHandle.write(root)
		# zipFileHandle.write(dirs)

		for _ in files:
			zipFileHandle.write(os.path.join(root, _))
			# zipFileHandle.write(_)
			# zipFileHandle.write(os.path.join(dirs, _))
# ---------------------------------------------------------------------------------------------------

DIR::handle.write(
		fullpath = os.path.join(
				root = for root, dirs, files in os.walk(path),
				f = ... for f in files
			)
		archiveName = os.path.join(
				archive_root = os.path.abspath(root)[len(os.path.abspath(path)):],
				f
			)
		compression # hackish way involves forcing ZIP_STORED level compression
	)

FILE::handle.write(
		path = path_to_file
		os.path.basename(path)
		compression
	)

# --------------
1lpivwM
1Lg78w5
