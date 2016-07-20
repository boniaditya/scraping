import urllib2

source = urllib2.urlopen('http://pyladies.com')

pyladies = source.read()
if((pyladies.find('Python')) != -1):
    print("The word python exists on pyladies home page")
else:
    print ("The word python does not exist on pyladies home page")

google = urllib2.urlopen('http://google.com')
googleread = google.read()
print(googleread[5])
print(googleread.find('img'))

if (googleread.find('img') != 1):
    print("There are images on the google home page")
else:
    print("There are no images on the google home page")
pythonorg = urllib2.urlopen('http://python.org')
pythonorgread = pythonorg.read()
print("The first ten characters on the python home page are" + " " + pythonorgread[:10])