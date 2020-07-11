import json

# data = '''
# {
#     "name" : "Vo Trung Tan",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+84 799 578 779"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }
# '''

# info = json.loads(data)
# print('Name:', info['name'])
# print('Hide:', info['email']['hide'])

data = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Vo Trung Tan"
    } ,
    {
        "id" : "007",
        "x" : "5",
        "name" : "Ha Duy Kien"
    } ,
    {
        "id" : "009",
        "x" : "9",
        "name" : "Le Thi Thuy An"
    } 
]
'''

info = json.loads(data)
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attr:', item['x'])



