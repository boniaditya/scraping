from urllib.request import urlopen
from bs4 import BeautifulSoup
htmldata = urlopen("http://www.pythonscraping.com/pages/page1.html")
Object = BeautifulSoup(htmldata.read())
print(Object.h1)