import json
import urllib2
from urllib2 import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))
print(urlopen("http://freegeoip.net/json/50.78.253.58").read().decode('utf-8'))
jsonString = urlopen("http://freegeoip.net/json/50.78.253.58").read().decode('utf-8')
print jsonString
jsonObj = json.loads(jsonString)

print jsonObj
print(jsonObj.get("ip"))
print(jsonObj.get("country_code"))
