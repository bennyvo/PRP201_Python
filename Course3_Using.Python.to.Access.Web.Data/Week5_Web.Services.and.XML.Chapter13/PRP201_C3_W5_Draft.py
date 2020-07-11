import xml.etree.ElementTree as ET

# data = '''
# <person>
#     <name>Vo Trung Tan</name>
#     <phone type="intl">+84 799 578 779</phone>
#     <email hide="yes"/>
# </person>
# '''
# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Vo Trung Tan</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Le Thi Thuy An</name>
        </user>
        <user x="11">
            <id>010</id>
            <name>Le Trong Nhan</name>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count.:', len(lst))
for item in lst:
    print('Name:',item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attr:', item.get('x'))




