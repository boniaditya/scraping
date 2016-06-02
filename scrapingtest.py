from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page.html")
print(html.read())