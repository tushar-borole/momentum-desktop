import urllib
import sys
import os

for i in range(01,16):
    URL="https://momentumdash.com/backgrounds/"+str(i).zfill(2)+".jpg"
    IMAGE = URL.rsplit('/',1)[1]
    fullfilename = os.path.join(sys.argv[1], IMAGE)
    print "Downloading "+URL+" to "+fullfilename
    urllib.urlretrieve(URL, fullfilename)
