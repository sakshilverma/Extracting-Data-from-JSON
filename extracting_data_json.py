import urllib.request, urllib.parse, urllib.error
import json

url=input("Enter URL - ")
f=urllib.request.urlopen(url).read().decode()
jf=json.loads(f)
sum=0
for c in jf['comments']:
    sum+=int(c['count'])

print(sum)
