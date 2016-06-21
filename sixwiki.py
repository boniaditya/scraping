from urllib import urlopen
from bs4 import BeautifulSoup
import re

htmlwiki = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bswikiObj = BeautifulSoup(htmlwiki.read())

for link in bswikiObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

