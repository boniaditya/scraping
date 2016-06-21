import requests
from bs4 import BeautifulSoup

# r = requests.get("http://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles+")
url = "http://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles+"
r = requests.get(url)

soup = BeautifulSoup(r.content)
# for link in soup.findAll("a"):
#    print (link)
# for link in soup.findAll("div",{"class":"info"}):
#    print (link)
# for link in soup.findAll("a",{"class":"like"}):
#    print (link)

# links = soup.findAll("a")

# for link in links:
#    print link.get("href")
#    print link.text
#    print link.text, link.get("href")
#    if "http" in link.get("href"):
#  print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

if soup.findAll("section", {"class": "info"}) is None:
    print "Section is None"
else:
    print "section is not None"

g_data = soup.findAll("div", {"class": "info"})
for item in g_data:
    #    print (item[0].text)
    #    print item.contents
    #    print (item.contents[0].text)
    #    print (item.contents[0].findAll("a", {"class": "business-name"})[0].text)
    for child in item.findAll("a", {"class": "business-name"}):
        print (child.text)
    for street in item.findAll("span", {"itemprop": "streetAddress"}):
        print (street.text)
    for locality in item.findAll("span", {"itemprop": "addressLocality"}):
        print (locality.text)
    for address in item.findAll("span", {"itemprop": "addressRegion"}):
        print (address.text)
    for code in item.findAll("span", {"itemprop": "postalCode"}):
        print (code.text)
'''
      print (item.contents[1].findAll("span", {"itemprop":"streetAddress"})[0].text)
        print (item.contents[1].findAll("span",{"itemprop":"addressLocality"})[0].text)
        print (item.contents[1].findAll("span",{"itemprop":"addressRegion"})[0].text)
        print (item.contents[1].findAll("span", {"itemprop": "postalCode"})[0].text)
'''
#    print (item.contents[0].findAll("a",{"itemprop":"name"})[0].text)
#    print (item.contents[0].findAll("a",{"class":"business-name"})[0].text)
#    print (item.contents[1].findAll("p",{"class":"adr"})[0].text)
#    print (item.contents[1].findAll("li",{"class":"primary"})[0].text)
# for item in g_data:
#    print (item.contents[0].text)
#    print (item.contents[1].text)
#    print (item.contents[1].findAll("p",{"itemprop":"address"})[0].text)
#   try:
#       print (item.contents[0].findAll("a",{"class":"business-name"})[0].text)
#       print (item.contents[1].findAll("p", {"itemprop": "address"})[0].text)
#       print (item.contents[1].findAll("p", {"itemprop": "address"})[0].findAll("span",{"itemprop":"streetAddress"})[0].text)
# print (item.contents[1].findAll("p", {"itemprop": "address"})[0].findAll("span", {"itemprop": "streetAddress"})[1].text)
#       print (item.contents[1].findAll("span", {"itemprop": "streetAddress"})[0].text)
#       print (item.contents[1].findAll("p", {"itemprop": "address"})[0].find("").text)
