import httplib
import urllib
import time

API_KEY = "54CDA6FJF4RCJ92C"

cmail = "samyaljamal@cmail.carleton.ca"
group = " L2-M-7"
identifier = " a"

phrase = cmail + group + identifier

print(phrase)

params = urllib.urlencode({'field1': phrase, 'key':API_KEY }) 
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")

try:
  conn.request("POST", "/update", params, headers)

  response = conn.getresponse()

  print response.status, response.reason

  data = response.read()
  conn.close()
except:
  print "connection failed"
