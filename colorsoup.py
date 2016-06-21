from urllib import urlopen
from bs4 import BeautifulSoup
from SoupTest import getTitle
html = urlopen("http://www.gsibspeak.com/index.php/about-gsib/vision-and-mission/8-course-showcase/3-mba-ib")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("td", {"bgcolor":"#FFFFCC"})
for name in nameList:
    print(name.get_text())

htmlnew = urlopen("http://www.pythonscraping.com/pages/page.html")

headingList = bsObj.findAll({"h1","h2","h3","h4","h5","h6"},True)
for heading in headingList:
    print(heading.get_text())

title = getTitle("http://www.pythonscraping.com/pages/page.html")


mbaCount = bsObj.findAll({"body","span"},True, text="MBA")
print(len(mbaCount))

allText = bsObj.findAll(class_="active")
print(allText[0].get_text())