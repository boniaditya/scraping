from urllib.request import urlopen
html = urlopen("http://www.healthcoachinginstitute.com")
print(html.read())