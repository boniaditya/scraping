from urllib import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read())
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])

htmlfull = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObjfull = BeautifulSoup(htmlfull.read())
fulltext = bsObjfull.findAll(lambda tag: len(tag.attrs) == 2)
print(fulltext[1].get_text())