import urllib
input_file = open('links.txt','r')
for line in input_file:
    URL= line
    IMAGE = URL.rsplit('/',1)[1]
    urllib.urlretrieve(URL, IMAGE)