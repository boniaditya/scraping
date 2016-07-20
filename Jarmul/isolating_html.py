from bs4 import BeautifulSoup
import urllib2
import requests

def get_tree(url):

    source = urllib2.urlopen(url).read()
    tree = BeautifulSoup(source, "html.parser")
    return tree

happyhours = 'https://www.downtownla.com/explore/dining-nightlife'
happy_source = urllib2.urlopen(happyhours).read()
r = requests.get(happyhours)
happy_soup = BeautifulSoup(r.content)
#print(happy_soup)

#print(happy_source.info().get('Content-Encoding'))
#if __name__ == '__main__':
    #First, I am going to identify the areas of the page I want to look at

 #   tree = get_tree('https://www.downtownla.com/explore/dining-nightlife/happy-hour-finder')
the_tree = get_tree('http://python.org')
happy_tree = get_tree('https://www.downtownla.com/explore/dining-nightlife/happy-hour-finder/bunker-hill-bar-grill')
#print(get_tree('http://google.com'))
#print(happy_tree)

ptags = happy_soup.find_all('p')
print(ptags)
print(len(ptags))

i=0
for me in happy_soup.find_all('div'):
    i += 1
    print i

print i

print(happy_soup.find('title').text)
print(happy_soup.find('body').text)

for li in happy_soup.find_all('li'):
    print li.text

"""
found_happy_hours = []

for t in happy_soup.find_all('div', {'class':'info'}):
    text = t.text
    print(text)

print(found_happy_hours)
"""