import urllib
import urllib2

url = "https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyCrv9b7dDoLSLA_vcRomCgaBrF4UtVVOZo"
values = {'longUrl' : 'google.com'}

data = urllib.urlencode(values)

req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

the_page = response.read()
