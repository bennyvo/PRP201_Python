import re

fname = 'mbox-short.txt'
fpath = ('/Users/vtt/Desktop⁩/PRP201_Python_MOOC/PRP201/⁨Resources/⁩')
fhandle = open(fpath+fname)

# for line in fhandle:
#     words = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

# import re
# for line in fhandle:
#     words = line.rstrip()
#     if re.search('From:', line):
#         print(line)


# for line in fhandle:
#     words = line.rstrip()
#     if line.startswith('From:') >= 0:
#         print(line)

# import re
# for line in fhandle:
#     words = line.rstrip()
#     if re.search('^From:', line):
#         print(line)

# x = 'My 2 favourite number is 39 and 100 EIONHISD'
# y = re.findall('[0-9]+', x)
# print(y)
# y = re.findall('[AEIOU]', x)
# print(y)

# x = 'From: Using the : Ahihi do ngoc ngech'
# y = re.findall('^F.+:', x)
# y = re.findall('^F.+?:', x)
# print(y)

# numblist = list()
# for line in fhandle:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1: continue
#     num = float(stuff[0])
#     numblist.append(num)
# print('Maximum:', max(numblist))

# line = 'From ahihi.ahuhu@tanvt.local Sat Jun  5 09:14:16 2020'
# x = re.findall('^From .*@([^ ]*)', line)
# print(x)

# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)

