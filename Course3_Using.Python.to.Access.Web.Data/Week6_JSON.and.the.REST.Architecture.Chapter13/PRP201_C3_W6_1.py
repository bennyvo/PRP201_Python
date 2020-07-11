import json
import urllib.request, urllib.parse, urllib.error

#Test_Case: http://py4e-data.dr-chuck.net/comments_42.json 
#Test_Case: http://py4e-data.dr-chuck.net/comments_581877.json

json_url = input('Enter location: ')

print('Retrieving ...', json_url)
data = urllib.request.urlopen(json_url).read().decode()
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

#Data calc
count = 0
summ = 0

for comment in json_obj['comments']:
    count += 1
    summ += int(comment['count'])
print('Count:', count)
print('Sum:', summ)





# import urllib.request as ur
# import json

# # json_url = 'http://python-data.dr-chuck.net/comments_42.json'

# json_url = input("Enter location: ")
# print("Retrieving ", json_url)
# data = ur.urlopen(json_url).read().decode('utf-8')
# print('Retrieved', len(data), 'characters')
# json_obj = json.loads(data)

# sum = 0
# total_number = 0

# for comment in json_obj["comments"]:
#     sum += int(comment["count"])
#     total_number += 1

# print('Count:', total_number)
# print('Sum:', sum)
