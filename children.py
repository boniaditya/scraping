from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

#for child in bsObj.find("table",{"id":"giftList"}).children:
 #   print(child)

#for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
  # print(sibling)

for karthik in bsObj.find("tr",{"class":"gift"}).previous_siblings:
    print(karthik)