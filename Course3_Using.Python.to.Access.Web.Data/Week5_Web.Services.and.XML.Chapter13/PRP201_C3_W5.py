import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter location: ')
html = urllib.request.urlopen(link).read().decode()
print('Retrieving ...', link)
print('Retrieved', len(html), 'characters')

#Data calc
count = 0
summ = 0

#Data extract
data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    count += 1
    summ += int(tag.find('count').text)
print('Count:', count)
print('Sum:', summ)

# Case Test: http://py4e-data.dr-chuck.net/comments_581876.xml