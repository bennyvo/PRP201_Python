from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Position 3 (the first name is 1). 
# Repeat this process 4 times. 
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah


# url: http://py4e-data.dr-chuck.net/known_by_Tayyib.html
# Find:
# Position 18 (the first name is 1). 
# Repeat this process 7 times.
# => The first character of the name of the last page that you will load is: R

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

names = list()
while count > 0:
    print('Retrieving: {0}'.format(url))
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1
print(names[-1])