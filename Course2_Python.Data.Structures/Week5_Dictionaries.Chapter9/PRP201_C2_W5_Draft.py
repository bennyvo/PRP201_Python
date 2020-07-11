# purse = dict()
# purse['A'] = 3
# purse['B'] = 4
# purse['C'] = 5
# purse['D'] = 6

# print(purse)
# purse['A'] = purse['A'] + 2
# print(purse)

# purse['A'] = 4
# print(purse)

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# # for name in names:
# #     if name not in counts:
# #         counts[name] = 1
# #     else:
# #         counts[name] = counts[name] + 1
# # print(counts)

# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# counts = dict()
# line = input('Enter line of text:')
# words = line.split()

# print('Words: ', words)
# print('Counting words in your text ... \n')
# for word in words:
#     counts[word] = counts.get(word, 0) +1
# print('Count result: ', counts)
# print(counts.items())

fname = input('Enter file name: ')
fpath = 'C:/Users/Admin/Desktop/[PRP201]/'

fhandle = open(fpath+fname)
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)
