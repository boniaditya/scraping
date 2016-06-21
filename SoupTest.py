import urllib2
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

html=urllib2.urlopen("https://docs.python.org/3.5/howto/urllib2.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1)

