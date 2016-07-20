from StringIO import StringIO
import gzip
import urllib2

request = urllib2.Request('https://www.downtownla.com/explore/dining-nightlife/happy-hour-finder/bunker-hill-bar-grill')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)
if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( response.read())
    f = gzip(fileobj=buf)
    data = f.read()