DEBUG---
"""
So documentation says it better to use bytes as filenames but doing that
produces error (shown below)

How will I handle unicode files then?
	chcp 65001
	try encode native_codepage
	except encode utf-8
"""

fileName = r"D:\code\-sandbox\Free Sex Stories & Erotic Stories @ XNXX.COM.html"
outputFileName = r"Free Sex Stories & Erotic Stories @ XNXX.COM.htmz"
with zipfile.ZipFile(outputFileName, mode='a', compression=zipfile.ZIP_STORED) as zfh:
	zfh.write(fileName.encode("UTF-8"), os.path.basename(fileName).encode("UTF-8"))
"""
>>> import zipfile
>>> fileName = r"D:\code\-sandbox\#2FreeX.COM.html"
>>> outputFileName = r"#2FreeX.COM.zip"
>>> with zipfile.ZipFile(outputFileName.encode("UTF-8"), mode='a', compression=zipfile.ZIP_STORED) as zfh:
...     zfh.write(fileName, os.path.basename(fileName))
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Program Files\Python35-32\lib\zipfile.py", line 1046, in __init__
    self._RealGetContents()
  File "C:\Program Files\Python35-32\lib\zipfile.py", line 1089, in _RealGetContents
    endrec = _EndRecData(fp)
  File "C:\Program Files\Python35-32\lib\zipfile.py", line 241, in _EndRecData
    fpin.seek(0, 2)
AttributeError: 'bytes' object has no attribute 'seek'
>>>
"""